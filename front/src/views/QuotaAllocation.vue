<template>
  <div class="quota-container">
    <el-row :gutter="20">
      <!-- 权重调节面板 -->
      <el-col :span="24">
        <div class="chart-box">
          <h3>分配因素权重调节</h3>
          <div class="weight-sliders">
            <div v-for="(weight, index) in weights" :key="index" class="weight-item">
              <span class="weight-label">{{ weight.name }}</span>
              <el-slider
                v-model="weight.value"
                :max="100"
                :min="0"
                @input="handleWeightChange"
              />
              <span class="weight-value">{{ weight.value }}%</span>
            </div>
          </div>
        </div>
      </el-col>

      <!-- 名额分配结果 -->
      <el-col :span="12">
        <div class="chart-box">
          <h3>各学院名额分配结果</h3>
          <div class="quota-info">
            <div v-for="(quota, college) in currentQuotas" :key="college" class="quota-item">
              <span>{{ college }}:</span>
              <span class="quota-number">{{ quota }}个</span>
            </div>
          </div>
          <v-chart class="chart" :option="quotaResultOption" autoresize />
        </div>
      </el-col>

      <!-- 权重雷达图 -->
      <el-col :span="12">
        <div class="chart-box">
          <h3>权重分布</h3>
          <v-chart class="chart" :option="weightRadarOption" autoresize />
        </div>
      </el-col>

      <!-- 因果关系桑基图 -->
      <el-col :span="24">
        <div class="chart-box">
          <h3>名额分配因果关系图</h3>
          <v-chart class="chart" :option="sankeyOption" autoresize />
        </div>
      </el-col>

      <!-- 敏感度分析 -->
      <el-col :span="24">
        <div class="chart-box">
          <h3>权重敏感度分析</h3>
          <div class="sensitivity-info">
            <div v-for="college in colleges" :key="college" class="sensitivity-item">
              <span class="college-name">{{ college }}</span>
              <div class="sensitivity-values">
                <div v-for="(weight, index) in weights" :key="index" class="sensitivity-value">
                  <span>{{ weight.name }}:</span>
                  <span :class="{ 
                    'positive': getSensitivityValue(college, weight.name) > 0,
                    'negative': getSensitivityValue(college, weight.name) < 0
                  }">
                    {{ getSensitivityValue(college, weight.name) > 0 ? '+' : '' }}
                    {{ getSensitivityValue(college, weight.name) }}
                  </span>
                </div>
              </div>
            </div>
          </div>
          <v-chart class="chart" :option="sensitivityOption" autoresize />
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, nextTick } from 'vue'
import { use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { BarChart, RadarChart, SankeyChart, LineChart } from 'echarts/charts'
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent,
  ToolboxComponent
} from 'echarts/components'
import VChart from 'vue-echarts'

use([
  CanvasRenderer,
  BarChart,
  RadarChart,
  SankeyChart,
  LineChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent,
  ToolboxComponent
])

// 首先定义基础数据
const colleges = ['计算机学院', '机械学院', '经管学院', '材料学院', '理学院']

// 权重因素
const weights = ref([
  { name: '科研成果', value: 30 },
  { name: '师资力量', value: 25 },
  { name: '学科评级', value: 20 },
  { name: '培养质量', value: 15 },
  { name: '招生计划', value: 10 }
])

const currentQuotas = ref({})

// 各学院在各个维度的得分
const collegeScores = {
  '计算机学院': { 科研成果: 90, 师资力量: 85, 学科评级: 95, 培养质量: 88, 招生计划: 92 },
  '机械学院': { 科研成果: 85, 师资力量: 88, 学科评级: 90, 培养质量: 85, 招生计划: 85 },
  '经管学院': { 科研成果: 80, 师资力量: 82, 学科评级: 85, 培养质量: 83, 招生计划: 80 },
  '材料学院': { 科研成果: 82, 师资力量: 80, 学科评级: 83, 培养质量: 80, 招生计划: 78 },
  '理学院': { 科研成果: 78, 师资力量: 75, 学科评级: 80, 培养质量: 78, 招生计划: 75 }
}

// 计算最终分配名额
const calculateQuotas = (currentWeights = weights.value) => {
  const totalQuota = 200 // 总名额
  const quotas = {}
  let totalScore = 0

  // 计算每个学院的加权得分
  colleges.forEach(college => {
    let score = 0
    currentWeights.forEach(weight => {
      score += (collegeScores[college][weight.name] * weight.value) / 100
    })
    quotas[college] = score
    totalScore += score
  })

  // 根据得分比例分配名额
  Object.keys(quotas).forEach(college => {
    quotas[college] = Math.round((quotas[college] / totalScore) * totalQuota)
  })

  return quotas
}

// 计算敏感度值
const getSensitivityValue = (college, weightName) => {
  // 保存原始权重
  const originalWeights = [...weights.value]
  const originalQuota = calculateQuotas()[college]
  
  // 创建新的权重数组，增加指定权重10%
  const newWeights = weights.value.map(w => ({
    name: w.name,
    value: w.name === weightName ? 
      Math.min(w.value + 10, 100) : 
      w.value
  }))
  
  // 重新计算总权重为100%
  const total = newWeights.reduce((sum, w) => sum + w.value, 0)
  newWeights.forEach(w => {
    w.value = Math.round((w.value / total) * 100)
  })
  
  // 计算新的配额
  const newQuota = calculateQuotas(newWeights)[college]
  
  // 计算变化量
  const change = newQuota - originalQuota
  
  return change
}

// 处理权重变化
const handleWeightChange = () => {
  // 确保权重总和为100
  const total = weights.value.reduce((sum, w) => sum + w.value, 0)
  if (total !== 100) {
    weights.value.forEach(w => {
      w.value = Math.round((w.value / total) * 100)
    })
  }
  
  // 更新当前配额
  currentQuotas.value = calculateQuotas()
  
  // 触发敏感度分析的重新计算
  nextTick(() => {
    // 如果需要，可以在这里添加额外的更新逻辑
  })
}

// 初始化配额
onMounted(() => {
  currentQuotas.value = calculateQuotas()
})

// 图表配置
const quotaResultOption = computed(() => {
  const quotas = calculateQuotas()
  return {
    title: {
      text: '各学院名额分配结果'
    },
    tooltip: {
      trigger: 'axis',
      formatter: '{b}: {c}个名额'
    },
    xAxis: {
      type: 'category',
      data: colleges
    },
    yAxis: {
      type: 'value',
      name: '分配名额'
    },
    series: [{
      type: 'bar',
      data: colleges.map(college => quotas[college]),
      itemStyle: {
        color: '#409EFF'
      },
      label: {
        show: true,
        position: 'top'
      }
    }]
  }
})

// 权重雷达图配置
const weightRadarOption = computed(() => ({
  title: {
    text: '权重分布'
  },
  radar: {
    indicator: weights.value.map(w => ({ name: w.name, max: 100 }))
  },
  series: [{
    type: 'radar',
    data: [{
      value: weights.value.map(w => w.value),
      name: '权重分布',
      areaStyle: {
        color: 'rgba(64,158,255,0.3)'
      }
    }]
  }]
}))

// 因果关系桑基图配置
const sankeyOption = computed(() => ({
  title: {
    text: '名额分配因果关系'
  },
  tooltip: {
    trigger: 'item',
    triggerOn: 'mousemove'
  },
  series: [{
    type: 'sankey',
    layout: 'none',
    emphasis: {
      focus: 'adjacency'
    },
    data: [
      ...weights.value.map(w => ({ name: w.name })),
      ...colleges.map(c => ({ name: c }))
    ],
    links: weights.value.reduce((links, weight) => {
      colleges.forEach(college => {
        links.push({
          source: weight.name,
          target: college,
          value: Math.round(collegeScores[college][weight.name] * weight.value / 100)
        })
      })
      return links
    }, [])
  }]
}))

// 敏感度分析图表配置
const sensitivityOption = computed(() => {
  // 计算每个权重变化10%时的名额变化
  const sensitivityData = colleges.map(college => {
    return {
      name: college,
      data: weights.value.map(weight => {
        return getSensitivityValue(college, weight.name)
      })
    }
  })

  return {
    title: {
      text: '权重敏感度分析'
    },
    tooltip: {
      trigger: 'axis',
      formatter: function(params) {
        let result = params[0].axisValue + '<br/>'
        params.forEach(param => {
          result += param.seriesName + ': ' 
          result += (param.value > 0 ? '+' : '') + param.value + '个名额<br/>'
        })
        return result
      }
    },
    legend: {
      data: colleges,
      type: 'scroll',
      orient: 'horizontal',
      top: 30
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      containLabel: true,
      top: 80
    },
    xAxis: {
      type: 'category',
      data: weights.value.map(w => w.name),
      axisLabel: {
        interval: 0,
        rotate: 30
      }
    },
    yAxis: {
      type: 'value',
      name: '名额变化量',
      axisLabel: {
        formatter: '{value}个'
      }
    },
    series: sensitivityData.map(item => ({
      name: item.name,
      type: 'line',
      smooth: true,
      symbol: 'circle',
      symbolSize: 8,
      data: item.data,
      label: {
        show: true,
        position: 'top',
        formatter: function(params) {
          return (params.value > 0 ? '+' : '') + params.value
        }
      },
      emphasis: {
        focus: 'series'
      }
    }))
  }
})
</script>

<style scoped>
.quota-container {
  padding: 20px;
}

.chart-box {
  background: #fff;
  padding: 20px;
  border-radius: 4px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
}

.weight-sliders {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.weight-item {
  flex: 1;
  min-width: 250px;
  display: flex;
  align-items: center;
  gap: 10px;
}

.weight-label {
  min-width: 80px;
}

.weight-value {
  min-width: 50px;
}

.quota-info {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  margin-bottom: 20px;
}

.quota-item {
  background: #f5f7fa;
  padding: 8px 15px;
  border-radius: 4px;
  display: flex;
  gap: 10px;
}

.quota-number {
  font-weight: bold;
  color: #409EFF;
}

.sensitivity-info {
  margin-bottom: 20px;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
}

.sensitivity-item {
  background: #f5f7fa;
  padding: 15px;
  border-radius: 4px;
}

.college-name {
  font-weight: bold;
  margin-bottom: 10px;
  display: block;
}

.sensitivity-values {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.sensitivity-value {
  display: flex;
  justify-content: space-between;
  font-size: 14px;
}

.positive {
  color: #67C23A;
}

.negative {
  color: #F56C6C;
}

.chart {
  height: 400px;
  width: 100%;
}

h3 {
  margin-top: 0;
  margin-bottom: 20px;
  color: #333;
}
</style> 