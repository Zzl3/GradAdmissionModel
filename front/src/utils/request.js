import axios from 'axios'
import { ElMessage } from 'element-plus'
import { API_BASE_URL } from '@/api/config'

// 创建axios实例
const service = axios.create({
  baseURL: `${API_BASE_URL}/api`,  // 只在这里添加一次 /api 前缀
  timeout: 5000, // 请求超时时间
  withCredentials: false,  // 改为 false
  headers: {
    'Content-Type': 'application/json'
  }
})

// request拦截器
service.interceptors.request.use(
  config => {
    // 在发送请求之前做些什么
    // 例如：添加token
    const token = localStorage.getItem('token')
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`
    }
    // 添加必要的请求头
    config.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    return config
  },
  error => {
    // 对请求错误做些什么
    console.log(error)
    return Promise.reject(error)
  }
)

// response拦截器
service.interceptors.response.use(
  response => {
    const res = response.data
    
    // 如果返回的状态码不是200，说明接口有问题，把错误信息显示出来
    if (!res.success) {
      ElMessage({
        message: res.message || '错误',
        type: 'error',
        duration: 5 * 1000
      })
      return Promise.reject(new Error(res.message || '错误'))
    } else {
      return res
    }
  },
  error => {
    // 详细的错误处理
    if (error.code === 'ERR_NETWORK') {
      ElMessage.error('网络连接失败，请检查后端服务是否启动')
    } else if (error.response) {
      ElMessage.error(`请求失败: ${error.response.status}`)
    } else if (error.request) {
      ElMessage.error('未收到响应，请检查网络连接')
    } else {
      ElMessage.error(`请求错误: ${error.message}`)
    }
    return Promise.reject(error)
  }
)

export default service 