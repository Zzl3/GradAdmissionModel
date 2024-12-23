import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LineCharts from '../views/charts/LineCharts.vue'
import BarCharts from '../views/charts/BarCharts.vue'
import PieCharts from '../views/charts/PieCharts.vue'
import ScatterCharts from '../views/charts/ScatterCharts.vue'
import RadarCharts from '../views/charts/RadarCharts.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
    meta: { requiresAuth: true },
    children: [
      { path: 'line', component: LineCharts },
      { path: 'bar', component: BarCharts },
      { path: 'pie', component: PieCharts },
      { path: 'scatter', component: ScatterCharts },
      { path: 'radar', component: RadarCharts },
      { 
        path: 'data-analysis', 
        name: 'DataAnalysis',
        component: () => import('../views/DataAnalysis.vue')
      },
      { 
        path: 'quota-allocation', 
        name: 'QuotaAllocation',
        component: () => import('../views/QuotaAllocation.vue')
      },
      { path: '', redirect: '/line' }
    ]
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/LoginView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
