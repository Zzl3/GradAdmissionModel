import request from '@/utils/request'
import { API_ROUTES } from './config'

// 手机号登录
export function phoneLogin(data) {
  return request({
    url: API_ROUTES.PHONE_LOGIN,
    method: 'post',
    data
  })
}

// 账号密码登录
export function accountLogin(data) {
  return request({
    url: API_ROUTES.ACCOUNT_LOGIN,
    method: 'post',
    data
  })
}

// 发送验证码（统一接口）
export function sendSmsCode(phone, type = 'login') {
  return request({
    url: API_ROUTES.SEND_CODE,
    method: 'post',
    data: { 
      phone,
      type // 可选值：login-登录，register-注册，forget-找回密码
    }
  })
}

// 注册
export function register(data) {
  return request({
    url: API_ROUTES.REGISTER,
    method: 'post',
    data
  })
}

// 重置密码
export function resetPassword(data) {
  return request({
    url: API_ROUTES.RESET_PASSWORD,
    method: 'post',
    data
  })
} 