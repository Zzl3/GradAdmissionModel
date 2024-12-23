<template>
  <div class="login-container">
    <div class="login-box">
      <!-- 左侧区域 -->
      <div class="login-left">
        <div class="left-content">
          <div class="decoration-circle circle-1"></div>
          <div class="decoration-circle circle-2"></div>
          <div class="decoration-circle circle-3"></div>
          
          <div class="left-text">
            <h2>研究生名额分配模型系统</h2>
            <div class="divider"></div>
            <!-- <p class="welcome-text">欢迎使用</p> -->
            <p class="desc-text">基于多目标优化的研究生招生计划分配模型</p>
            <div class="feature-list">
              <div class="feature-item">
                <el-icon><DataLine /></el-icon>
                <span>数据可视化</span>
              </div>
              <div class="feature-item">
                <el-icon><Operation /></el-icon>
                <span>智能分配</span>
              </div>
              <div class="feature-item">
                <el-icon><TrendCharts /></el-icon>
                <span>预测分析</span>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <!-- 右侧表单区域 -->
      <div class="login-right">
        <el-card class="login-card">
          <!-- 登录界面 -->
          <template v-if="activeTab !== 'register' && activeTab !== 'forget'">
            <el-tabs v-model="loginType" class="login-tabs">
              <el-tab-pane label="账号登录" name="account">
                <el-form :model="accountForm" :rules="accountRules" ref="accountFormRef">
                  <el-form-item prop="phone">
                    <el-input 
                      v-model="accountForm.phone" 
                      placeholder="请输入手机号"
                      :prefix-icon="User"
                    />
                  </el-form-item>
                  <el-form-item prop="password">
                    <el-input 
                      v-model="accountForm.password" 
                      type="password" 
                      placeholder="密码"
                      :prefix-icon="Lock"
                      show-password
                      autocomplete="new-password"
                    />
                  </el-form-item>
                  <div class="form-actions">
                    <el-button 
                      type="primary" 
                      @click="handleAccountLogin" 
                      class="submit-btn"
                      :loading="loading"
                    >
                      登录
                    </el-button>
                  </div>
                </el-form>
              </el-tab-pane>
              <el-tab-pane label="验证码登录" name="phone">
                <el-form :model="phoneForm" :rules="phoneRules" ref="phoneFormRef">
                  <el-form-item prop="phone">
                    <el-input 
                      v-model="phoneForm.phone" 
                      placeholder="请输入手机号"
                      :prefix-icon="Iphone"
                    />
                  </el-form-item>
                  <el-form-item prop="code">
                    <div class="code-input">
                      <el-input 
                        v-model="phoneForm.code" 
                        placeholder="请输入验证码"
                        :prefix-icon="Message"
                      />
                      <el-button 
                        type="primary" 
                        class="code-btn"
                        :disabled="isCountDown"
                        @click="handleSendCode"
                      >
                        {{ countDownText }}
                      </el-button>
                    </div>
                  </el-form-item>
                  <el-form-item>
                    <el-button 
                      type="primary" 
                      @click="handlePhoneLogin" 
                      class="submit-btn"
                      :loading="loading"
                    >
                      登录
                    </el-button>
                  </el-form-item>
                </el-form>
              </el-tab-pane>
            </el-tabs>

            <!-- 统一的底部链接区域 -->
            <div class="bottom-links">
              <div class="links-group">
                <div class="link-item">
                  <el-button 
                    link 
                    type="primary" 
                    @click="activeTab = 'register'"
                    class="action-link"
                  >
                    立即注册
                  </el-button>
                  <span class="divider">|</span>
                  <el-button 
                    link 
                    type="primary" 
                    @click="() => {
                      activeTab = 'forget';
                      loginType = 'forget';
                    }"
                    class="action-link"
                  >
                    找回密码
                  </el-button>
                </div>
              </div>
            </div>
          </template>

          <!-- 注册界面 -->
          <template v-else-if="activeTab === 'register'">
            <div class="register-content">
              <!-- <h3 class="form-title">用户注册</h3> -->
              <el-form :model="registerForm" :rules="registerRules" ref="registerFormRef">
                <el-form-item prop="phone">
                  <el-input 
                    v-model="registerForm.phone" 
                    placeholder="请输入手机号"
                    :prefix-icon="Iphone"
                  />
                </el-form-item>
                <el-form-item prop="code">
                  <div class="code-input">
                    <el-input 
                      v-model="registerForm.code" 
                      placeholder="请输入验证码"
                      :prefix-icon="Message"
                    />
                    <el-button 
                      type="primary" 
                      class="code-btn"
                      :disabled="isCountDown"
                      @click="handleSendRegisterCode"
                    >
                      {{ countDownText }}
                    </el-button>
                  </div>
                </el-form-item>
                <el-form-item prop="password">
                  <el-input 
                    v-model="registerForm.password" 
                    type="password" 
                    placeholder="请设置密码"
                    :prefix-icon="Lock"
                    show-password
                    autocomplete="new-password"
                  />
                </el-form-item>
                <el-form-item prop="confirmPassword">
                  <el-input 
                    v-model="registerForm.confirmPassword" 
                    type="password" 
                    placeholder="请确认密码"
                    :prefix-icon="Lock"
                    show-password
                    autocomplete="new-password"
                  />
                </el-form-item>
                <el-form-item>
                  <el-button 
                    type="primary" 
                    @click="handleRegister" 
                    class="submit-btn"
                    :loading="loading"
                  >
                    注册
                  </el-button>
                </el-form-item>
              </el-form>
              
              <!-- 注册时显示登录链接 -->
              <div class="bottom-links">
                <span class="text-muted">已有账号？</span>
                <el-button 
                  link 
                  type="primary" 
                  @click="() => {
                    activeTab = 'account';
                    loginType = 'account';
                  }"
                  class="login-link"
                >
                  立即登录
                </el-button>
              </div>
            </div>
          </template>

          <!-- 忘记密码界面 -->
          <template v-else>
            <div class="forget-content">
              <el-form :model="forgetPasswordForm" :rules="forgetPasswordRules" ref="forgetPasswordFormRef">
                <el-form-item prop="phone">
                  <el-input 
                    v-model="forgetPasswordForm.phone" 
                    placeholder="请输入手机号"
                    :prefix-icon="Iphone"
                  />
                </el-form-item>
                <el-form-item prop="code" class="verification-code-item">
                  <div class="code-input">
                    <el-input 
                      v-model="forgetPasswordForm.code" 
                      placeholder="请输入验证码"
                      :prefix-icon="Message"
                    />
                    <el-button 
                      type="primary" 
                      class="code-btn"
                      :disabled="isCountDown"
                      @click="handleSendForgetCode"
                    >
                      {{ countDownText }}
                    </el-button>
                  </div>
                </el-form-item>
                <el-form-item prop="newPassword">
                  <el-input 
                    v-model="forgetPasswordForm.newPassword"
                    type="password" 
                    placeholder="请输入新密码"
                    :prefix-icon="Lock"
                    show-password
                    autocomplete="new-password"
                  />
                </el-form-item>
                <el-form-item prop="confirmPassword">
                  <el-input 
                    v-model="forgetPasswordForm.confirmPassword"
                    type="password" 
                    placeholder="请确认新密码"
                    :prefix-icon="Lock"
                    show-password
                    autocomplete="new-password"
                  />
                </el-form-item>
                <el-form-item>
                  <el-button 
                    type="primary" 
                    @click="handleForgetSubmit" 
                    class="submit-btn"
                    :loading="loading"
                  >
                    重置密码
                  </el-button>
                </el-form-item>
              </el-form>
              <div class="bottom-links">
                <span>已有账号？</span>
                <el-button 
                  link 
                  type="primary" 
                  @click="() => {
                    activeTab = 'account';
                    loginType = 'account';
                  }"
                >
                  立即登录
                </el-button>
              </div>
            </div>
          </template>
        </el-card>
      </div>
    </div>
  </div>

  <!-- 找回密码对话框 -->
  <el-dialog
    v-model="showForgetDialog"
    title="找回密码"
    width="400px"
    :close-on-click-modal="false"
  >
    <el-steps :active="forgetStep" finish-status="success">
      <el-step title="验证手机" />
      <el-step title="重置密码" />
    </el-steps>

    <!-- 第一步：验证手机号 -->
    <template v-if="forgetStep === 0">
      <el-form
        ref="forgetFormRef"
        :model="forgetPasswordForm"
        :rules="forgetPasswordRules"
        label-width="0"
      >
        <el-form-item prop="phone">
          <el-input 
            v-model="forgetPasswordForm.phone"
            placeholder="请输入手机号"
            :prefix-icon="Iphone"
          />
        </el-form-item>
        <el-form-item prop="code">
          <div class="code-input">
            <el-input 
              v-model="forgetPasswordForm.code"
              placeholder="请输入验证码"
              :prefix-icon="Message"
            />
            <el-button 
              type="primary"
              :disabled="isCountDown"
              @click="handleSendForgetCode"
            >
              {{ countDownText }}
            </el-button>
          </div>
        </el-form-item>
      </el-form>
    </template>

    <!-- 第二步：重置密码 -->
    <template v-else>
      <el-form
        ref="forgetPasswordFormRef"
        :model="forgetPasswordForm"
        :rules="forgetPasswordRules"
        label-width="0"
      >
        <el-form-item prop="newPassword">
          <el-input 
            v-model="forgetPasswordForm.newPassword"
            type="password"
            placeholder="请输入新密码"
            :prefix-icon="Lock"
            show-password
            autocomplete="new-password"
          />
        </el-form-item>
        <el-form-item prop="confirmPassword">
          <el-input 
            v-model="forgetPasswordForm.confirmPassword"
            type="password"
            placeholder="请确认新密码"
            :prefix-icon="Lock"
            show-password
            autocomplete="new-password"
          />
        </el-form-item>
      </el-form>
    </template>

    <template #footer>
      <el-button @click="showForgetDialog = false">取消</el-button>
      <el-button 
        type="primary" 
        @click="handleForgetNext"
        :loading="loading"
      >
        {{ forgetStep === 0 ? '下一步' : '确定' }}
      </el-button>
    </template>
  </el-dialog>
</template>

<script setup>
import { ref, reactive, computed, onUnmounted, watch } from 'vue'
import { useRouter } from 'vue-router'
import { User, Lock, Iphone, Message } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus'
import { phoneLogin, accountLogin, sendSmsCode, register, resetPassword } from '@/api/auth'
import { API_URLS } from '@/api/config'
import axios from 'axios'

const router = useRouter()
const activeTab = ref('account')
const loginType = ref('account')
const loading = ref(false)
const countDown = ref(0)
const timer = ref(null)

// 表单引用
const phoneFormRef = ref(null)
const accountFormRef = ref(null)
const registerFormRef = ref(null)

// 手机验证码登录表单
const phoneForm = reactive({
  phone: '',
  code: ''
})

// 账号登录表单
const accountForm = reactive({
  phone: '',
  password: ''
})

// 注册表单
const registerForm = reactive({
  phone: '',
  code: '',
  password: '',
  confirmPassword: ''
})

// 表单验证规则
const phoneRules = {
  phone: [
    { required: true, message: '请输入手机号', trigger: 'blur' },
    { pattern: /^1[3-9]\d{9}$/, message: '请输入正确的手机号', trigger: 'blur' }
  ],
  code: [
    { required: true, message: '请输入验证码', trigger: 'blur' },
    { len: 6, message: '验证码长度应为6位', trigger: 'blur' }
  ]
}

const accountRules = {
  phone: [
    { required: true, message: '请输入手机号', trigger: 'blur' },
    { pattern: /^1[3-9]\d{9}$/, message: '请输入正确的手机号', trigger: 'blur' }
  ],
  password: [
    { required: true, message: '请入密码', trigger: 'blur' },
    { min: 6, message: '密码长度不能小于6位', trigger: 'blur' }
  ]
}

const registerRules = {
  phone: [
    { required: true, message: '请输入手机号', trigger: 'blur' },
    { pattern: /^1[3-9]\d{9}$/, message: '请输入正确的手机号', trigger: 'blur' }
  ],
  code: [
    { required: true, message: '请输入验证码', trigger: 'blur' },
    { len: 6, message: '验证码长度应为6位', trigger: 'blur' }
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' },
    { min: 6, message: '密码长度不能小于6位', trigger: 'blur' }
  ],
  confirmPassword: [
    { required: true, message: '请确认密码', trigger: 'blur' },
    {
      validator: (rule, value, callback) => {
        if (value !== registerForm.password) {
          callback(new Error('两次输入的密码不一致'))
        } else {
          callback()
        }
      },
      trigger: 'blur'
    }
  ]
}

// 计算属性
const isCountDown = computed(() => countDown.value > 0)
const countDownText = computed(() => isCountDown.value ? `${countDown.value}s` : '获取验证码')

// 发送验证码
const startCountDown = () => {
  countDown.value = 60
  timer.value = setInterval(() => {
    countDown.value--
    if (countDown.value <= 0) {
      clearInterval(timer.value)
      timer.value = null
    }
  }, 1000)
}

const handleSendCode = async () => {
  try {
    await phoneFormRef.value.validateField('phone')
    const res = await sendSmsCode(phoneForm.phone, 'login')
    if (res.success) {
      ElMessage.success('验证码已发送')
      startCountDown()
    }
  } catch (error) {
    console.error('发送验证码失败:', error)
    ElMessage.error(error.message || '发送验证码失败')
  }
}

const handleSendRegisterCode = async () => {
  try {
    await registerFormRef.value.validateField('phone')
    const res = await sendSmsCode(registerForm.phone, 'register')
    if (res.success) {
      ElMessage.success('验证码已发送')
      startCountDown()
    }
  } catch (error) {
    console.error('发送验证码失败:', error)
    ElMessage.error(error.message || '发送验证码失败')
  }
}

// 手机验证登录处理函数
const handlePhoneLogin = async () => {
  if (!phoneFormRef.value) {
    return
  }
  
  try {
    await phoneFormRef.value.validate()
    loading.value = true
    
    const response = await phoneLogin({
      phone: phoneForm.phone,
      code: phoneForm.code
    })
    
    if (response.success) {
      ElMessage.success('登录成功')
      resetAllForms()
      router.push('/')
    }
  } catch (error) {
    console.error('手机验证码登录失败:', error)
    ElMessage.error(error.message || '登录失败')
  } finally {
    loading.value = false
  }
}

// 账号登录处理函数
const handleAccountLogin = async () => {
  if (!accountFormRef.value) return
  try {
    await accountFormRef.value.validate()
    loading.value = true
    
    const response = await accountLogin({
      phone: accountForm.phone,
      password: accountForm.password
    })
    
    if (response.success) {
      ElMessage.success('登录成功')
      resetAllForms()
      router.push('/')
    }
  } catch (error) {
    console.error('账号登录失败:', error)
    ElMessage.error(error.message || '登录失败')
  } finally {
    loading.value = false
  }
}

// 注册处理函数
const handleRegister = async () => {
  if (!registerFormRef.value) return
  try {
    await registerFormRef.value.validate()
    loading.value = true
    
    const response = await register({
      phone: registerForm.phone,
      code: registerForm.code,
      password: registerForm.password
    })
    
    if (response.success) {
      ElMessage.success('注册成功')
      resetAllForms()
      activeTab.value = 'account'
    }
  } catch (error) {
    console.error('注册失败:', error)
    ElMessage.error(error.message || '注册失败')
  } finally {
    loading.value = false
  }
}

// 重置表单
const resetForm = () => {
  registerForm.phone = ''
  registerForm.code = ''
  registerForm.password = ''
  registerForm.confirmPassword = ''
  if (timer.value) {
    clearInterval(timer.value)
    timer.value = null
  }
  countDown.value = 0
}

// 组件卸载时清理定时器
onUnmounted(() => {
  if (timer.value) {
    clearInterval(timer.value)
  }
})

// 修找回密码相关数据
const forgetPasswordFormRef = ref(null)
const forgetPasswordForm = reactive({
  phone: '',
  code: '',
  newPassword: '',
  confirmPassword: ''
})

// 处理找回密码提交
const handleForgetSubmit = async () => {
  if (!forgetPasswordFormRef.value) return
  try {
    await forgetPasswordFormRef.value.validate()
    loading.value = true
    const res = await resetPassword({
      phone: forgetPasswordForm.phone,
      code: forgetPasswordForm.code,
      newPassword: forgetPasswordForm.newPassword
    })
    
    if (res.success) {
      ElMessage.success('密码重置成功')
      resetAllForms()
      activeTab.value = 'account'
      loginType.value = 'account'
    }
  } catch (error) {
    console.error('重置密码失败:', error)
    ElMessage.error(error.message || '重置密码失败')
  } finally {
    loading.value = false
  }
}

// 重置找回密码表单
const resetForgetPasswordForm = () => {
  forgetPasswordForm.phone = ''
  forgetPasswordForm.code = ''
  forgetPasswordForm.newPassword = ''
  forgetPasswordForm.confirmPassword = ''
  if (forgetPasswordFormRef.value) {
    forgetPasswordFormRef.value.resetFields()
  }
}

// 发送找回密码验证码
const handleSendForgetCode = async () => {
  try {
    await forgetPasswordFormRef.value.validateField('phone')
    const res = await sendSmsCode(forgetPasswordForm.phone, 'forget')
    if (res.success) {
      ElMessage.success('验证码发送成功')
      startCountDown()
    }
  } catch (error) {
    console.error('发送验证码失败:', error)
    ElMessage.error(error.message || '发送验证码失败')
  }
}

// 找回密码验证规则
const forgetPasswordRules = {
  phone: [
    { required: true, message: '请输入手机号', trigger: 'blur' },
    { pattern: /^1[3-9]\d{9}$/, message: '请输入正确的手机号', trigger: 'blur' }
  ],
  code: [
    { required: true, message: '请输入验证码', trigger: 'blur' },
    { len: 6, message: '验证码长度必须为6位', trigger: 'blur' }
  ],
  newPassword: [
    { required: true, message: '请输入新密码', trigger: 'blur' },
    { min: 6, max: 20, message: '密码长度必须在6-20位之间', trigger: 'blur' }
  ],
  confirmPassword: [
    { required: true, message: '请确认新密码', trigger: 'blur' },
    {
      validator: (rule, value, callback) => {
        if (value !== forgetPasswordForm.newPassword) {
          callback(new Error('两次输入的密码不一致'))
        } else {
          callback()
        }
      },
      trigger: 'blur'
    }
  ]
}

// 统一的表单重置函数
const resetAllForms = () => {
  // 重置登录表单
  phoneForm.phone = ''
  phoneForm.code = ''
  if (phoneFormRef.value) {
    phoneFormRef.value.resetFields()
  }

  // 重置账号登录表单
  accountForm.phone = ''
  accountForm.password = ''
  if (accountFormRef.value) {
    accountFormRef.value.resetFields()
  }

  // 重置注册表单
  registerForm.phone = ''
  registerForm.code = ''
  registerForm.password = ''
  registerForm.confirmPassword = ''
  if (registerFormRef.value) {
    registerFormRef.value.resetFields()
  }

  // 重置找回密码表单
  forgetPasswordForm.phone = ''
  forgetPasswordForm.code = ''
  forgetPasswordForm.newPassword = ''
  forgetPasswordForm.confirmPassword = ''
  if (forgetPasswordFormRef.value) {
    forgetPasswordFormRef.value.resetFields()
  }

  // 重置倒计时
  if (timer.value) {
    clearInterval(timer.value)
    timer.value = null
  }
  countDown.value = 0
}
</script>

<style scoped>
.login-container {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: linear-gradient(135deg, #1e80ff 0%, #1e80ff 100%);
  position: relative;
  overflow: hidden;
}

.login-container::before {
  content: '';
  position: absolute;
  width: 2000px;
  height: 2000px;
  border-radius: 50%;
  background: linear-gradient(135deg, #ffffff20 0%, #ffffff10 100%);
  top: -10%;
  right: 48%;
  transform: translateY(-50%);
  z-index: 1;
  animation: move 18s infinite linear;
}

@keyframes move {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

.login-box {
  display: flex;
  width: 900px;
  height: 600px;
  background: white;
  border-radius: 20px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  z-index: 2;
}

.login-left {
  flex: 1;
  background: linear-gradient(135deg, #1e80ff 0%, #1e90ff 100%);
  padding: 40px;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  color: white;
}

.left-content {
  position: relative;
  z-index: 2;
  width: 100%;
}

.decoration-circle {
  position: absolute;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.1);
}

.circle-1 {
  width: 200px;
  height: 200px;
  top: -100px;
  left: -100px;
  animation: float 8s infinite ease-in-out;
}

.circle-2 {
  width: 300px;
  height: 300px;
  bottom: -150px;
  right: -150px;
  animation: float 12s infinite ease-in-out reverse;
}

.circle-3 {
  width: 150px;
  height: 150px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  animation: pulse 6s infinite ease-in-out;
}

@keyframes float {
  0%, 100% {
    transform: translate(0, 0);
  }
  50% {
    transform: translate(20px, 20px);
  }
}

@keyframes pulse {
  0%, 100% {
    transform: scale(1) translate(-50%, -50%);
    opacity: 0.5;
  }
  50% {
    transform: scale(1.2) translate(-40%, -40%);
    opacity: 0.8;
  }
}

.left-text {
  text-align: center;
  padding: 20px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 15px;
  backdrop-filter: blur(10px);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}

.left-text h2 {
  font-size: 28px;
  font-weight: 600;
  margin-bottom: 20px;
  color: white;
}

.divider {
  width: 60px;
  height: 4px;
  background: white;
  margin: 20px auto;
  border-radius: 2px;
}

.welcome-text {
  font-size: 20px;
  margin-bottom: 10px;
  color: rgba(255, 255, 255, 0.9);
}

.desc-text {
  font-size: 16px;
  color: rgba(255, 255, 255, 0.8);
  margin-bottom: 30px;
  line-height: 1.6;
}

.feature-list {
  display: flex;
  justify-content: center;
  gap: 30px;
  margin-top: 40px;
}

.feature-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  transition: transform 0.3s ease;
}

.feature-item:hover {
  transform: translateY(-5px);
}

.feature-item .el-icon {
  font-size: 24px;
  background: rgba(255, 255, 255, 0.2);
  padding: 10px;
  border-radius: 10px;
  transition: all 0.3s ease;
}

.feature-item:hover .el-icon {
  background: rgba(255, 255, 255, 0.3);
  transform: scale(1.1);
}

.feature-item span {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.9);
}

/* 响应式调整 */
@media screen and (max-width: 992px) {
  .login-box {
    width: 90%;
    flex-direction: column;
  }

  .login-left {
    padding: 30px;
  }

  .feature-list {
    flex-wrap: wrap;
    gap: 20px;
  }

  .left-text h2 {
    font-size: 24px;
  }

  .welcome-text {
    font-size: 18px;
  }

  .desc-text {
    font-size: 14px;
  }
}

/* 添加玻璃拟态效果 */
.login-left::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(
    45deg,
    rgba(255, 255, 255, 0.1) 0%,
    rgba(255, 255, 255, 0.05) 100%
  );
  backdrop-filter: blur(10px);
  z-index: 1;
}

.login-right {
  flex: 1;
  padding: 40px 60px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.login-card {
  background: transparent;
  border: none;
  box-shadow: none;
}

.title-box {
  text-align: center;
  margin-bottom: 30px;
  padding-bottom: 20px;
  border-bottom: 1px solid #eee;
}

.title-box h3 {
  font-size: 24px;
  color: #1e80ff;
  margin: 0;
  margin-bottom: 10px;
  font-weight: 600;
}

.subtitle {
  font-size: 16px;
  color: #666;
  margin: 0;
}

.submit-btn {
  margin-top: 10px;
  background: linear-gradient(135deg, #1e80ff 0%, #1e90ff 100%);
  border-radius: 25px;
}

.submit-btn:hover {
  opacity: 0.9;
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(30, 128, 255, 0.3);
}

:deep(.el-tabs__item) {
  font-size: 16px;
  color: #666;
  padding: 0 25px;
}

:deep(.el-tabs__item.is-active) {
  color: #1e80ff;
  font-weight: 500;
}

:deep(.el-tabs__active-bar) {
  background-color: #1e80ff;
  height: 3px;
  border-radius: 3px;
}

:deep(.el-input__wrapper) {
  background-color: #f5f7fa;
  border: none;
  box-shadow: none;
  transition: all 0.3s ease;
}

:deep(.el-input__wrapper:hover) {
  background-color: #eef1f6;
}

:deep(.el-input__wrapper.is-focus) {
  background-color: #fff;
  box-shadow: 0 0 0 1px #1e80ff;
}

:deep(.el-input__inner) {
  height: 40px;
}

:deep(.el-form-item__error) {
  color: #ff4d4f;
  font-size: 12px;
  padding-top: 4px;
}

:deep(.el-input__prefix-inner) {
  color: #1e80ff;
}

:deep(.el-loading-spinner .circular) {
  width: 24px;
  height: 24px;
}

:deep(.el-loading-spinner .path) {
  stroke: #1e80ff;
}

.code-input {
  display: flex;
  gap: 10px;
}

.code-btn {
  width: 120px;
  border-radius: 4px;
}

:deep(.el-tabs__nav) {
  width: 100%;
  display: flex;
}

:deep(.el-tabs__item) {
  flex: 1;
  text-align: center;
}

.submit-btn {
  width: 100%;
  height: 40px;
  border-radius: 20px;
  font-size: 16px;
  background: linear-gradient(135deg, #1e80ff 0%, #1e90ff 100%);
  border: none;
  transition: all 0.3s ease;
}

.submit-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(30, 128, 255, 0.3);
}

/* 底部切换提示样式 */
.switch-tip {
  text-align: center;
  margin-top: 20px;
  color: #666;
  font-size: 14px;
}

/* 标签页样式优化 */
:deep(.el-tabs__nav-wrap) {
  padding: 0 40px;
}

:deep(.el-tabs__nav) {
  display: flex;
  justify-content: space-around;
  width: 100%;
}

:deep(.el-tabs__item) {
  flex: 1;
  text-align: center;
  font-size: 16px;
  height: 50px;
  line-height: 50px;
  transition: all 0.3s ease;
  font-weight: 500;
  color: #666;
  padding: 0 30px;
}

:deep(.el-tabs__item:hover) {
  color: #1e80ff;
}

:deep(.el-tabs__item.is-active) {
  color: #1e80ff;
  font-weight: 600;
}

:deep(.el-tabs__active-bar) {
  height: 3px;
  border-radius: 3px;
  background: linear-gradient(90deg, #1e80ff, #1e90ff);
}

/* 右侧表单区域样式优化 */
.login-right {
  flex: 1;
  padding: 40px 60px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.login-card {
  background: transparent;
  border: none;
  box-shadow: none;
}

/* 标签页样式优化 */
:deep(.el-tabs__nav-wrap) {
  padding: 0;
  margin-bottom: 40px;
}

:deep(.el-tabs__nav) {
  width: 100%;
  display: flex;
  justify-content: center;
  gap: 80px;
}

:deep(.el-tabs__item) {
  font-size: 20px;
  padding: 0 15px;
  height: 50px;
  line-height: 50px;
  color: #909399;
  transition: all 0.3s ease;
  font-weight: 500;
}

:deep(.el-tabs__item.is-active) {
  color: #1e80ff;
  font-weight: 600;
}

:deep(.el-tabs__active-bar) {
  height: 4px;
  border-radius: 2px;
  background: linear-gradient(90deg, #1e80ff, #1e90ff);
}

/* 表单样式优化 */
:deep(.el-form-item) {
  margin-bottom: 25px;
}

:deep(.el-input__wrapper) {
  background-color: #f5f7fa;
  border: 1px solid transparent;
  border-radius: 12px;
  padding: 0 20px;
  height: 48px;
  transition: all 0.3s ease;
}

:deep(.el-input__wrapper:hover) {
  background-color: #eef1f6;
}

:deep(.el-input__wrapper.is-focus) {
  background-color: #fff;
  border-color: #1e80ff;
  box-shadow: 0 0 0 1px #1e80ff;
}

:deep(.el-input__inner) {
  height: 48px;
  font-size: 16px;
}

:deep(.el-input__prefix-inner) {
  color: #909399;
  font-size: 18px;
}

/* 验证码按钮样式 */
.code-input {
  display: flex;
  gap: 12px;
}

.code-btn {
  min-width: 120px;
  height: 48px;
  border-radius: 12px;
  font-size: 14px;
  font-weight: 500;
  background: linear-gradient(135deg, #1e80ff 0%, #1e90ff 100%);
  border: none;
  color: white;
  transition: all 0.3s ease;
}

.code-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(30, 128, 255, 0.3);
}

/* 登录按钮样式 */
.submit-btn {
  width: 100%;
  height: 48px;
  border-radius: 12px;
  font-size: 16px;
  font-weight: 500;
  background: linear-gradient(135deg, #1e80ff 0%, #1e90ff 100%);
  border: none;
  margin-top: 30px;
  transition: all 0.3s ease;
}

.submit-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(30, 128, 255, 0.3);
}

/* 注册表单标题 */
.form-title {
  text-align: center;
  font-size: 28px;
  color: #1e80ff;
  margin-bottom: 40px;
  font-weight: 600;
}

/* 底部链接样式 */
.bottom-links {
  margin-top: 20px;
  text-align: center;
}

.links-group {
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.link-item {
  display: flex;
  align-items: center;
  gap: 8px;
}

.divider {
  color: #dcdfe6;
  margin: 0 2px;
}

.action-link {
  font-size: 14px;
  padding: 0;
  height: auto;
  line-height: 1.5;
  position: relative;
  transition: all 0.3s ease;
}

.action-link:hover {
  color: #1e80ff;
  transform: translateY(-1px);
}

.action-link::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 100%;
  height: 1px;
  background-color: #1e80ff;
  transform: scaleX(0);
  transition: transform 0.3s ease;
  transform-origin: right;
}

.action-link:hover::after {
  transform: scaleX(1);
  transform-origin: left;
}

/* 适配移动端 */
@media screen and (max-width: 768px) {
  .links-group {
    flex-direction: column;
    align-items: center;
    gap: 15px;
  }
  
  .link-item {
    justify-content: center;
  }
}
</style>
