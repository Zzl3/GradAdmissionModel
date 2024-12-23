<template>
  <div class="charts-container">
    <el-row :gutter="20">
      <!-- 基础散点图 -->
      <el-col :span="12">
        <div class="chart-box">
          <h3>基础散点图</h3>
          <v-chart class="chart" :option="basicScatterOption" />
        </div>
      </el-col>

      <!-- 气泡图 -->
      <el-col :span="12">
        <div class="chart-box">
          <h3>气泡图</h3>
          <v-chart class="chart" :option="bubbleOption" />
        </div>
      </el-col>

      <!-- 散点矩阵 -->
      <el-col :span="12">
        <div class="chart-box">
          <h3>散点矩阵</h3>
          <v-chart class="chart" :option="matrixScatterOption" />
        </div>
      </el-col>

      <!-- 带有涟漪效果散点图 -->
      <el-col :span="12">
        <div class="chart-box">
          <h3>涟漪散点图</h3>
          <v-chart class="chart" :option="effectScatterOption" />
        </div>
      </el-col>

      <!-- 多维度散点图 -->
      <el-col :span="24">
        <div class="chart-box">
          <h3>多维度散点图</h3>
          <v-chart class="chart" :option="multiDimensionOption" />
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
import { use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { ScatterChart, EffectScatterChart } from 'echarts/charts'
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent,
  VisualMapComponent
} from 'echarts/components'
import VChart from 'vue-echarts'

// 注册必需的组件
use([
  CanvasRenderer,
  ScatterChart,
  EffectScatterChart,  // 涟漪效果散点图需要
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent,
  VisualMapComponent  // 多维度散点图需要
])

// 生成随机数据
const generateData = (count) => {
  const data = []
  for (let i = 0; i < count; i++) {
    data.push([
      Math.random() * 100,
      Math.random() * 100,
      Math.random() * 100
    ])
  }
  return data
}

// 基础散点图配置
const basicScatterOption = {
  xAxis: {},
  yAxis: {},
  series: [{
    symbolSize: 20,
    data: [
      [10.0, 8.04],
      [8.07, 6.95],
      [13.0, 7.58],
      [9.05, 8.81],
      [11.0, 8.33],
      [14.0, 7.66],
      [13.4, 6.81],
      [10.0, 6.33],
      [14.0, 8.96],
      [12.5, 6.82],
      [9.15, 7.20],
      [11.5, 7.20],
      [3.03, 4.23],
      [12.2, 7.83],
      [2.02, 4.47],
      [1.05, 3.33],
      [4.05, 4.96],
      [6.03, 7.24],
      [12.0, 6.26],
      [12.0, 8.84],
      [7.08, 5.82],
      [5.02, 5.68]
    ],
    type: 'scatter'
  }]
}

// 气泡图配置
const bubbleOption = {
  tooltip: {
    trigger: 'item',
    formatter: function (params) {
      return `X: ${params.value[0]}<br/>Y: ${params.value[1]}<br/>Size: ${params.value[2]}`
    }
  },
  xAxis: {},
  yAxis: {},
  series: [{
    type: 'scatter',
    symbolSize: function (data) {
      return Math.sqrt(data[2]) * 5
    },
    data: generateData(50)
  }]
}

// 散点矩阵配置
const matrixScatterOption = {
  tooltip: {
    trigger: 'item'
  },
  legend: {
    data: ['Group A', 'Group B']
  },
  xAxis: {},
  yAxis: {},
  series: [
    {
      name: 'Group A',
      type: 'scatter',
      data: generateData(20)
    },
    {
      name: 'Group B',
      type: 'scatter',
      data: generateData(20)
    }
  ]
}

// 涟漪散点图配置
const effectScatterOption = {
  xAxis: {},
  yAxis: {},
  series: [{
    type: 'effectScatter',
    symbolSize: 20,
    data: generateData(20),
    rippleEffect: {
      brushType: 'stroke'
    }
  }]
}

// 多维度散点图配置
const multiDimensionOption = {
  tooltip: {
    trigger: 'item'
  },
  visualMap: {
    min: 0,
    max: 100,
    dimension: 2,
    orient: 'vertical',
    right: 10,
    top: 'center',
    text: ['HIGH', 'LOW'],
    calculable: true,
    inRange: {
      color: ['#f2c31a', '#24b7f2']
    }
  },
  xAxis: {},
  yAxis: {},
  series: [{
    type: 'scatter',
    symbolSize: function (data) {
      return Math.sqrt(data[2]) * 3
    },
    data: generateData(100)
  }]
}
</script>

<style scoped>
.charts-container {
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