// API 基础配置
export const API_BASE_URL = 'http://127.0.0.1:5000'

// API 路径配置
export const API_ROUTES = {
  PHONE_LOGIN: '/phone-login',
  ACCOUNT_LOGIN: '/account-login',
  REGISTER: '/register',
  SEND_CODE: '/send-code',
  FORGET_PASSWORD_CODE: '/forget-password/code',
  RESET_PASSWORD: '/reset-password'
}

// 完整的 API URL
export const API_URLS = {
  PHONE_LOGIN: `${API_BASE_URL}/api${API_ROUTES.PHONE_LOGIN}`,
  ACCOUNT_LOGIN: `${API_BASE_URL}/api${API_ROUTES.ACCOUNT_LOGIN}`,
  REGISTER: `${API_BASE_URL}/api${API_ROUTES.REGISTER}`,
  SEND_CODE: `${API_BASE_URL}/api${API_ROUTES.SEND_CODE}`,
  FORGET_PASSWORD_CODE: `${API_BASE_URL}/api${API_ROUTES.FORGET_PASSWORD_CODE}`,
  RESET_PASSWORD: `${API_BASE_URL}/api${API_ROUTES.RESET_PASSWORD}`
} 