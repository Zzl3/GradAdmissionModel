<template>
  <div class="charts-container">
    <el-row :gutter="20">
      <!-- 基础雷达图 -->
      <el-col :span="12">
        <div class="chart-box">
          <h3>基础雷达图</h3>
          <v-chart class="chart" :option="basicRadarOption" />
        </div>
      </el-col>

      <!-- 多雷达图 -->
      <el-col :span="12">
        <div class="chart-box">
          <h3>多雷达图</h3>
          <v-chart class="chart" :option="multiRadarOption" />
        </div>
      </el-col>

      <!-- 填充雷达图 -->
      <el-col :span="12">
        <div class="chart-box">
          <h3>填充雷达图</h3>
          <v-chart class="chart" :option="filledRadarOption" />
        </div>
      </el-col>

      <!-- 圆形雷达图 -->
      <el-col :span="12">
        <div class="chart-box">
          <h3>圆形雷达图</h3>
          <v-chart class="chart" :option="circleRadarOption" />
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
import { use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { RadarChart } from 'echarts/charts'
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent
} from 'echarts/components'
import VChart from 'vue-echarts'

// 注册必需的组件
use([
  CanvasRenderer,
  RadarChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent
])

// 基础雷达图配置
const basicRadarOption = {
  title: {
    text: '基础雷达图'
  },
  legend: {
    data: ['预算分配', '实际开销']
  },
  radar: {
    indicator: [
      { name: '销售', max: 6500 },
      { name: '管理', max: 16000 },
      { name: '信息技术', max: 30000 },
      { name: '客服', max: 38000 },
      { name: '研发', max: 52000 },
      { name: '市场', max: 25000 }
    ]
  },
  series: [{
    name: '预算 vs 开销',
    type: 'radar',
    data: [
      {
        value: [4200, 3000, 20000, 35000, 50000, 18000],
        name: '预算分配'
      },
      {
        value: [5000, 14000, 28000, 26000, 42000, 21000],
        name: '实际开销'
      }
    ]
  }]
}

// 多雷达图配置
const multiRadarOption = {
  title: {
    text: '多雷达图'
  },
  tooltip: {
    trigger: 'axis'
  },
  legend: {
    left: 'center',
    data: ['A型球员', 'B型球员', 'C型球员']
  },
  radar: [
    {
      indicator: [
        { text: '进攻', max: 100 },
        { text: '防守', max: 100 },
        { text: '体能', max: 100 },
        { text: '速度', max: 100 },
        { text: '力量', max: 100 },
        { text: '技术', max: 100 }
      ],
      center: ['25%', '50%'],
      radius: 80
    },
    {
      indicator: [
        { text: '进攻', max: 100 },
        { text: '防守', max: 100 },
        { text: '体能', max: 100 },
        { text: '速度', max: 100 },
        { text: '力量', max: 100 },
        { text: '技术', max: 100 }
      ],
      radius: 80,
      center: ['75%', '50%']
    }
  ],
  series: [
    {
      type: 'radar',
      radarIndex: 0,
      data: [
        {
          value: [85, 70, 75, 80, 70, 90],
          name: 'A型球员'
        },
        {
          value: [90, 80, 95, 70, 60, 85],
          name: 'B型球员'
        },
        {
          value: [75, 85, 70, 75, 80, 70],
          name: 'C型球员'
        }
      ]
    },
    {
      type: 'radar',
      radarIndex: 1,
      data: [
        {
          value: [85, 70, 75, 80, 70, 90],
          name: 'A型球员'
        },
        {
          value: [90, 80, 95, 70, 60, 85],
          name: 'B型球员'
        },
        {
          value: [75, 85, 70, 75, 80, 70],
          name: 'C型球员'
        }
      ]
    }
  ]
}

// 填充雷达图配置
const filledRadarOption = {
  title: {
    text: '填充雷达图'
  },
  legend: {
    data: ['预算分配', '实际开销']
  },
  radar: {
    indicator: [
      { name: '销售', max: 100 },
      { name: '管理', max: 100 },
      { name: '信息技术', max: 100 },
      { name: '客服', max: 100 },
      { name: '研发', max: 100 },
      { name: '市场', max: 100 }
    ]
  },
  series: [{
    name: '预算 vs 开销',
    type: 'radar',
    areaStyle: {},
    data: [
      {
        value: [85, 70, 75, 80, 70, 90],
        name: '预算分配'
      },
      {
        value: [90, 80, 95, 70, 60, 85],
        name: '实际开销'
      }
    ]
  }]
}

// 圆形雷达图配置
const circleRadarOption = {
  title: {
    text: '圆形雷达图'
  },
  legend: {
    data: ['预算分配']
  },
  radar: {
    shape: 'circle',
    indicator: [
      { name: '销售', max: 100 },
      { name: '管理', max: 100 },
      { name: '信息技术', max: 100 },
      { name: '客服', max: 100 },
      { name: '研发', max: 100 },
      { name: '市场', max: 100 }
    ]
  },
  series: [{
    name: '预算分配',
    type: 'radar',
    data: [
      {
        value: [85, 70, 75, 80, 70, 90],
        name: '预算',
        lineStyle: {
          type: 'dashed'
        }
      }
    ]
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