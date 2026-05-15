import { createApp } from 'vue'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router'
import HomePage from './pages/HomePage.vue'
import AuthPage from './pages/AuthPage.vue'

// 路由配置
const routes = [
  { path: '/', component: HomePage },
  { path: '/auth', component: AuthPage },
  { path: '/login', redirect: '/auth' },
  { path: '/register', redirect: '/auth' }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

const app = createApp(App)
app.use(router)
app.mount('#app')
