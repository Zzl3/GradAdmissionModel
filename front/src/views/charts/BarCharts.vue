<template>
  <div class="charts-container">
    <el-row :gutter="20">
      <!-- 基础柱状图 -->
      <el-col :span="12">
        <div class="chart-box">
          <h3>基础柱状图</h3>
          <v-chart class="chart" :option="basicBarOption" />
        </div>
      </el-col>

      <!-- 堆叠柱状图 -->
      <el-col :span="12">
        <div class="chart-box">
          <h3>堆叠柱状图</h3>
          <v-chart class="chart" :option="stackedBarOption" />
        </div>
      </el-col>

      <!-- 条形图 -->
      <el-col :span="12">
        <div class="chart-box">
          <h3>条形图</h3>
          <v-chart class="chart" :option="horizontalBarOption" />
        </div>
      </el-col>

      <!-- 正负条形图 -->
      <el-col :span="12">
        <div class="chart-box">
          <h3>正负条形图</h3>
          <v-chart class="chart" :option="negativeBarOption" />
        </div>
      </el-col>

      <!-- 瀑布图 -->
      <el-col :span="24">
        <div class="chart-box">
          <h3>瀑布图</h3>
          <v-chart class="chart" :option="waterfallOption" />
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
import { use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { BarChart } from 'echarts/charts'
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
  BarChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent
])

// 基础柱状图配置
const basicBarOption = {
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'shadow'
    }
  },
  xAxis: {
    type: 'category',
    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
  },
  yAxis: {
    type: 'value'
  },
  series: [{
    data: [120, 200, 150, 80, 70, 110, 130],
    type: 'bar'
  }]
}

// 堆叠柱状图配置
const stackedBarOption = {
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'shadow'
    }
  },
  legend: {
    data: ['直接访问', '邮件营销', '联盟广告', '视频广告', '搜索引擎']
  },
  xAxis: {
    type: 'category',
    data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
  },
  yAxis: {
    type: 'value'
  },
  series: [
    {
      name: '直接访问',
      type: 'bar',
      stack: 'total',
      data: [320, 332, 301, 334, 390, 330, 320]
    },
    {
      name: '邮件营销',
      type: 'bar',
      stack: 'total',
      data: [120, 132, 101, 134, 90, 230, 210]
    },
    {
      name: '联盟广告',
      type: 'bar',
      stack: 'total',
      data: [220, 182, 191, 234, 290, 330, 310]
    },
    {
      name: '视频广告',
      type: 'bar',
      stack: 'total',
      data: [150, 232, 201, 154, 190, 330, 410]
    },
    {
      name: '搜索引擎',
      type: 'bar',
      stack: 'total',
      data: [820, 932, 901, 934, 1290, 1330, 1320]
    }
  ]
}

// 条形图配置
const horizontalBarOption = {
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'shadow'
    }
  },
  xAxis: {
    type: 'value'
  },
  yAxis: {
    type: 'category',
    data: ['巴西', '印尼', '美国', '印度', '中国', '世界人口']
  },
  series: [
    {
      type: 'bar',
      data: [18203, 23489, 29034, 104970, 131744, 630230]
    }
  ]
}

// 正负条形图配置
const negativeBarOption = {
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'shadow'
    }
  },
  xAxis: {
    type: 'value'
  },
  yAxis: {
    type: 'category',
    data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
  },
  series: [
    {
      name: '收入',
      type: 'bar',
      stack: 'Total',
      data: [320, 302, 301, 334, 390, 330, 320]
    },
    {
      name: '支出',
      type: 'bar',
      stack: 'Total',
      data: [-120, -132, -101, -134, -190, -230, -210]
    }
  ]
}

// 瀑布图配置
const waterfallOption = {
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'shadow'
    },
    formatter: function (params) {
      let tar = params[1]
      return tar.name + '<br/>' + tar.seriesName + ' : ' + tar.value
    }
  },
  xAxis: {
    type: 'category',
    data: ['上月结余', '工资', '奖金', '投资收入', '其他收入', '日常开销', '其他支出', '本月结余']
  },
  yAxis: {
    type: 'value'
  },
  series: [
    {
      name: '辅助',
      type: 'bar',
      stack: 'Total',
      itemStyle: {
        borderColor: 'transparent',
        color: 'transparent'
      },
      emphasis: {
        itemStyle: {
          borderColor: 'transparent',
          color: 'transparent'
        }
      },
      data: [0, 1000, 2000, 3000, 4000, 3000, 2000, 1000]
    },
    {
      name: '收支',
      type: 'bar',
      stack: 'Total',
      label: {
        show: true,
        position: 'inside'
      },
      data: [1000, 1000, 1000, 1000, 1000, -1000, -1000, -1000]
    }
  ]
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