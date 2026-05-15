<template>
  <div id="app">
    <main class="app-main">
      <router-view />
    </main>
    <footer class="app-footer">
      <p>格式转换工具 v1.0.0</p>
    </footer>
  </div>
</template>

<script>
import { authApi } from './services/api.ts'

export default {
  name: 'App',
  data() {
    return {
      isLoggedIn: false,
      currentUser: ''
    }
  },
  mounted() {
    this.checkLogin()
  },
  methods: {
    checkLogin() {
      this.isLoggedIn = authApi.isLoggedIn()
      if (this.isLoggedIn) {
        const userStr = localStorage.getItem('user')
        if (userStr) {
          const user = JSON.parse(userStr)
          this.currentUser = user.username
        }
      }
    },
    handleLogout() {
      authApi.logout()
      this.isLoggedIn = false
      this.currentUser = ''
      this.$router.push('/')
    }
  }
}
</script>

<style>
#app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.app-main {
  flex: 1;
  background: #f5f5f5;
}

.app-footer {
  background: #333;
  color: white;
  text-align: center;
  padding: 20px;
}
</style>
