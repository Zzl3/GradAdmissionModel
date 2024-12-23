<template>
  <div class="home">
    <el-container>
      <!-- 顶部导航栏 -->
      <el-header height="60px">
        <div class="header-container">
          <!-- 左侧菜单 -->
          <el-menu
            :default-active="activeIndex"
            mode="horizontal"
            router
            class="left-menu"
            :ellipsis="false"
          >
            <el-menu-item index="/data-analysis">数据分析</el-menu-item>
            <el-menu-item index="/quota-allocation">名额分配</el-menu-item>
            <el-menu-item index="/line">折线图示例</el-menu-item>
            <el-menu-item index="/bar">柱状图示例</el-menu-item>
            <el-menu-item index="/pie">饼图示例</el-menu-item>
            <el-menu-item index="/scatter">散点图示例</el-menu-item>
            <el-menu-item index="/radar">雷达图示例</el-menu-item>
          </el-menu>
          
          <!-- 右侧用户信息和退出按钮 -->
          <div class="right-menu">
            <el-dropdown trigger="click">
              <span class="user-dropdown">
                <el-icon><User /></el-icon>
                <span>用户中心</span>
                <el-icon class="el-icon--right"><CaretBottom /></el-icon>
              </span>
              <template #dropdown>
                <el-dropdown-menu>
                  <el-dropdown-item @click="handleLogout">
                    <el-icon><SwitchButton /></el-icon>
                    <span>退出登录</span>
                  </el-dropdown-item>
                </el-dropdown-menu>
              </template>
            </el-dropdown>
          </div>
        </div>
      </el-header>

      <!-- 主要内容区域 -->
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import { User, CaretBottom, SwitchButton } from '@element-plus/icons-vue'

const router = useRouter()
const activeIndex = ref('/line')

// 处理退出登录
const handleLogout = () => {
  localStorage.removeItem('token')
  ElMessage.success('退出登录成功')
  router.push('/login')
}
</script>

<style scoped>
.home {
  width: 100%;
  height: 100vh;
}

.el-header {
  padding: 0;
  background-color: #fff;
  border-bottom: 1px solid #dcdfe6;
}

.header-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 100%;
}

.left-menu {
  border-bottom: none;
}

.left-menu :deep(.el-menu-item) {
  height: 60px;
  line-height: 60px;
}

.right-menu {
  height: 60px;
  display: flex;
  align-items: center;
  padding: 0 20px;
}

.user-dropdown {
  height: 60px;
  display: flex;
  align-items: center;
  padding: 0 10px;
  cursor: pointer;
  color: var(--el-text-color-primary);
  transition: background-color 0.3s;
}

.user-dropdown:hover {
  background-color: var(--el-menu-hover-bg-color);
}

.user-dropdown .el-icon {
  margin: 0 5px;
  font-size: 16px;
}

.user-dropdown span {
  font-size: 14px;
}

:deep(.el-dropdown-menu__item) {
  display: flex;
  align-items: center;
  padding: 8px 16px;
}

:deep(.el-dropdown-menu__item .el-icon) {
  margin-right: 8px;
  font-size: 16px;
}

.el-main {
  background-color: #f5f7fa;
  padding: 20px;
}

/* 确保下拉菜单样式正确 */
:deep(.el-dropdown-menu) {
  padding: 5px 0;
  border-radius: 4px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}
</style>
