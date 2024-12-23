import axios from 'axios'
import { API_URLS } from './config'

export const authService = {
  login(username, password) {
    return axios.post(API_URLS.LOGIN, { username, password })
  },
  
  register(username, password) {
    return axios.post(API_URLS.REGISTER, { username, password })
  }
} 