<template>
  <div class="analysis-container">
    <el-row :gutter="20">
      <!-- 各学院师资力量分析 -->
      <el-col :span="24">
        <div class="chart-box">
          <h3>各学院师资力量分析</h3>
          <v-chart class="chart" :option="teacherAnalysisOption" autoresize />
        </div>
      </el-col>

      <!-- 各学院论文发表情况 -->
      <el-col :span="12">
        <div class="chart-box">
          <h3>各学院论文发表情况</h3>
          <v-chart class="chart" :option="paperPublishOption" autoresize />
        </div>
      </el-col>

      <!-- 各学院科研项目情况 -->
      <el-col :span="12">
        <div class="chart-box">
          <h3>各学院科研项目情况</h3>
          <v-chart class="chart" :option="researchProjectOption" autoresize />
        </div>
      </el-col>

      <!-- 各学院学生评价对比 -->
      <el-col :span="24">
        <div class="chart-box">
          <h3>各学院学生评价对比</h3>
          <v-chart class="chart" :option="studentEvalOption" autoresize />
        </div>
      </el-col>

      <!-- 各学院发展趋势对比 -->
      <el-col :span="24">
        <div class="chart-box">
          <h3>各学院发展趋势对比</h3>
          <v-chart class="chart" :option="developmentTrendOption" autoresize />
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
import { use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { BarChart, LineChart, RadarChart } from 'echarts/charts'
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent,
  DataZoomComponent
} from 'echarts/components'
import VChart from 'vue-echarts'

use([
  CanvasRenderer,
  BarChart,
  LineChart,
  RadarChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent,
  DataZoomComponent
])

// 学院列表
const colleges = ['计算机学院', '机械学院', '经管学院', '材料学院', '理学院']

// 各学院师资力量分析
const teacherAnalysisOption = {
  title: {
    text: '各学院师资力量分析'
  },
  tooltip: {
    trigger: 'axis',
    axisPointer: { type: 'shadow' }
  },
  legend: {
    data: ['35岁以下', '35-45岁', '45-55岁', '55岁以上', '博导比例']
  },
  grid: {
    left: '3%',
    right: '4%',
    bottom: '3%',
    containLabel: true
  },
  xAxis: {
    type: 'category',
    data: colleges
  },
  yAxis: [
    {
      type: 'value',
      name: '教师数量',
      position: 'left'
    },
    {
      type: 'value',
      name: '博导比例',
      position: 'right',
      axisLabel: {
        formatter: '{value}%'
      }
    }
  ],
  series: [
    {
      name: '35岁以下',
      type: 'bar',
      stack: 'total',
      data: [20, 15, 12, 18, 14]
    },
    {
      name: '35-45岁',
      type: 'bar',
      stack: 'total',
      data: [30, 25, 20, 22, 18]
    },
    {
      name: '45-55岁',
      type: 'bar',
      stack: 'total',
      data: [15, 20, 18, 15, 16]
    },
    {
      name: '55岁以上',
      type: 'bar',
      stack: 'total',
      data: [10, 12, 8, 10, 9]
    },
    {
      name: '博导比例',
      type: 'line',
      yAxisIndex: 1,
      data: [45, 40, 35, 38, 42]
    }
  ]
}

// 各学院论文发表情况
const paperPublishOption = {
  title: {
    text: '各学院论文发表情况'
  },
  tooltip: {
    trigger: 'axis'
  },
  legend: {
    data: ['SCI论文', 'EI论文', '核心期刊', '平均影响因子']
  },
  grid: {
    left: '3%',
    right: '4%',
    bottom: '3%',
    containLabel: true
  },
  xAxis: {
    type: 'category',
    data: colleges
  },
  yAxis: [
    {
      type: 'value',
      name: '论文数量'
    },
    {
      type: 'value',
      name: '影响因子',
      position: 'right'
    }
  ],
  series: [
    {
      name: 'SCI论文',
      type: 'bar',
      data: [50, 45, 30, 40, 35]
    },
    {
      name: 'EI论文',
      type: 'bar',
      data: [30, 35, 25, 28, 22]
    },
    {
      name: '核心期刊',
      type: 'bar',
      data: [40, 38, 35, 32, 30]
    },
    {
      name: '平均影响因子',
      type: 'line',
      yAxisIndex: 1,
      data: [3.5, 3.2, 2.8, 3.0, 2.9]
    }
  ]
}

// 各学院科研项目情况
const researchProjectOption = {
  title: {
    text: '各学院科研项目情况'
  },
  tooltip: {
    trigger: 'axis',
    axisPointer: { type: 'shadow' }
  },
  legend: {
    data: ['国家级项目', '省部级项目', '横向项目', '项目经费']
  },
  grid: {
    left: '3%',
    right: '4%',
    bottom: '3%',
    containLabel: true
  },
  xAxis: {
    type: 'category',
    data: colleges
  },
  yAxis: [
    {
      type: 'value',
      name: '项目数量'
    },
    {
      type: 'value',
      name: '经费(万元)',
      position: 'right'
    }
  ],
  series: [
    {
      name: '国家级项目',
      type: 'bar',
      data: [15, 12, 8, 10, 9]
    },
    {
      name: '省部级项目',
      type: 'bar',
      data: [25, 22, 18, 20, 16]
    },
    {
      name: '横向项目',
      type: 'bar',
      data: [30, 28, 35, 25, 20]
    },
    {
      name: '项目经费',
      type: 'line',
      yAxisIndex: 1,
      data: [1200, 1000, 800, 900, 750]
    }
  ]
}

// 各学院学生评价对比
const studentEvalOption = {
  title: {
    text: '各学院学生评价对比'
  },
  tooltip: {
    trigger: 'axis'
  },
  legend: {
    data: colleges
  },
  radar: {
    indicator: [
      { name: '导师指导', max: 100 },
      { name: '课程质量', max: 100 },
      { name: '科研环境', max: 100 },
      { name: '学术氛围', max: 100 },
      { name: '资源支持', max: 100 }
    ]
  },
  series: [{
    type: 'radar',
    data: [
      {
        name: '计算机学院',
        value: [90, 85, 88, 85, 80],
        areaStyle: {opacity: 0.3}
      },
      {
        name: '机械学院',
        value: [85, 90, 82, 88, 85],
        areaStyle: {opacity: 0.3}
      },
      {
        name: '经管学院',
        value: [88, 82, 85, 80, 88],
        areaStyle: {opacity: 0.3}
      },
      {
        name: '材料学院',
        value: [82, 85, 90, 85, 82],
        areaStyle: {opacity: 0.3}
      },
      {
        name: '理学院',
        value: [85, 88, 85, 82, 85],
        areaStyle: {opacity: 0.3}
      }
    ]
  }]
}

// 各学院发展趋势对比
const developmentTrendOption = {
  title: {
    text: '各学院近五年发展趋势'
  },
  tooltip: {
    trigger: 'axis'
  },
  legend: {
    data: colleges
  },
  grid: {
    left: '3%',
    right: '4%',
    bottom: '3%',
    containLabel: true
  },
  xAxis: {
    type: 'category',
    boundaryGap: false,
    data: ['2019', '2020', '2021', '2022', '2023']
  },
  yAxis: {
    type: 'value',
    name: '综合得分'
  },
  series: colleges.map(college => ({
    name: college,
    type: 'line',
    smooth: true,
    data: Array(5).fill(0).map(() => Math.floor(Math.random() * 20 + 80))
  }))
}
</script>

<style scoped>
.analysis-container {
  padding: 20px;
}

.chart-box {
  background: #fff;
  padding: 20px;
  border-radius: 4px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
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