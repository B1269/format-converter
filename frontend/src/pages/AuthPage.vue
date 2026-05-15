<template>
  <div class="auth-page">
    <div class="auth-container">
      <!-- Logo 区域 -->
      <div class="auth-logo">
        <div class="logo-icon">📄</div>
        <div class="logo-text">
          <h1>格式转换工具</h1>
          <p>让文档处理更简单</p>
        </div>
      </div>

      <!-- 登录方式切换 -->
      <div class="login-tabs">
        <div
          class="login-tab"
          :class="{ active: loginType === 'account' }"
          @click="loginType = 'account'"
        >
          账号登录
        </div>
        <div
          class="login-tab"
          :class="{ active: loginType === 'phone' }"
          @click="loginType = 'phone'"
        >
          手机登录
        </div>
      </div>

      <!-- 账号登录表单 -->
      <form v-if="loginType === 'account'" @submit.prevent="handleLogin" class="auth-form">
        <!-- 管理员提示 -->
        <div class="admin-hint">
          💡 <strong>管理员账号：</strong>admin &nbsp;|&nbsp; 密码：Admin@123456<br>
          <strong>普通用户：</strong>testuser &nbsp;|&nbsp; 密码：Test@123456
        </div>

        <div class="form-group">
          <label class="form-label">用户名</label>
          <input
            v-model="accountForm.username"
            type="text"
            class="form-input"
            placeholder="请输入用户名"
            required
          />
        </div>
        <div class="form-group">
          <label class="form-label">密码</label>
          <input
            v-model="accountForm.password"
            type="password"
            class="form-input"
            placeholder="请输入密码"
            required
          />
        </div>
        <div class="form-error" v-if="loginError">{{ loginError }}</div>
        <button type="submit" class="login-btn" :disabled="loading">
          {{ loading ? '登录中...' : '登录' }}
        </button>
        <div class="form-links">
          <a href="#">忘记密码？</a>
          <span class="divider-line">|</span>
          <a href="#">注册新账号</a>
        </div>
      </form>

      <!-- 手机登录表单 -->
      <form v-else @submit.prevent="handlePhoneLogin" class="auth-form">
        <div class="form-group">
          <label class="form-label">手机号码</label>
          <input
            v-model="phoneForm.phone"
            type="tel"
            class="form-input"
            placeholder="请输入手机号码"
            maxlength="11"
            required
          />
        </div>
        <div class="form-group">
          <label class="form-label">验证码</label>
          <div class="code-input-group">
            <input
              v-model="phoneForm.code"
              type="text"
              class="form-input"
              placeholder="请输入验证码"
              maxlength="6"
              required
            />
            <button type="button" class="code-btn" @click="sendCode" :disabled="codeCooldown > 0">
              {{ codeCooldown > 0 ? `${codeCooldown}s` : '获取验证码' }}
            </button>
          </div>
        </div>
        <div class="form-error" v-if="phoneError">{{ phoneError }}</div>
        <button type="submit" class="login-btn" :disabled="loading">
          {{ loading ? '登录中...' : '登录 / 注册' }}
        </button>
      </form>

      <!-- 第三方登录 -->
      <div class="social-login">
        <div class="social-title">其他登录方式</div>
        <div class="social-buttons">
          <button type="button" class="social-btn wechat" @click="handleWechatLogin" title="微信登录">
            💬
          </button>
          <button type="button" class="social-btn qq" @click="handleQQLogin" title="QQ登录">
            🐧
          </button>
        </div>
      </div>

      <!-- 协议勾选 -->
      <div class="protocol-check">
        <input type="checkbox" id="protocolCheck" v-model="agreedToProtocol" />
        <label for="protocolCheck">
          我已阅读并同意
          <a href="#">《用户协议》</a> 和
          <a href="#">《隐私政策》</a>
        </label>
      </div>
    </div>
  </div>
</template>

<script>
import { authApi } from '../services/api.ts';

export default {
  name: 'AuthPage',
  data() {
    return {
      loginType: 'account', // 'account' | 'phone'
      loading: false,
      loginError: '',
      phoneError: '',
      agreedToProtocol: true,
      codeCooldown: 0,
      accountForm: {
        username: '',
        password: ''
      },
      phoneForm: {
        phone: '',
        code: ''
      }
    }
  },
  methods: {
    async handleLogin() {
      if (!this.agreedToProtocol) {
        this.loginError = '请先阅读并同意用户协议';
        return;
      }

      this.loading = true;
      this.loginError = '';

      try {
        const result = await authApi.login(
          this.accountForm.username,
          this.accountForm.password
        );

        if (result.success) {
          // 保存token
          localStorage.setItem('token', result.token);
          localStorage.setItem('user', JSON.stringify(result.user));
          // 跳转到首页
          this.$router.push('/');
        } else {
          this.loginError = result.error || '登录失败，请检查用户名和密码';
        }
      } catch (error) {
        this.loginError = '网络错误，请稍后重试';
      } finally {
        this.loading = false;
      }
    },

    async handlePhoneLogin() {
      if (!this.agreedToProtocol) {
        this.phoneError = '请先阅读并同意用户协议';
        return;
      }

      this.loading = true;
      this.phoneError = '';

      // 模拟手机登录
      setTimeout(() => {
        this.loading = false;
        alert('手机登录功能正在开发中，请使用账号登录');
      }, 1000);
    },

    handleWechatLogin() {
      alert('微信快捷登录功能正在开发中，请使用账号登录');
    },

    handleQQLogin() {
      alert('QQ快捷登录功能正在开发中，请使用账号登录');
    },

    sendCode() {
      if (this.codeCooldown > 0) return;

      const phone = this.phoneForm.phone;
      if (!phone || phone.length !== 11) {
        this.phoneError = '请输入正确的手机号码';
        return;
      }

      this.phoneError = '';
      this.codeCooldown = 60;

      const timer = setInterval(() => {
        this.codeCooldown--;
        if (this.codeCooldown <= 0) {
          clearInterval(timer);
        }
      }, 1000);

      alert('验证码已发送（模拟）');
    }
  }
}
</script>

<style scoped>
.auth-page {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 20px;
}

.auth-container {
  background: white;
  border-radius: 20px;
  padding: 40px;
  width: 100%;
  max-width: 420px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.2);
}

/* Logo 区域 */
.auth-logo {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 32px;
}

.logo-icon {
  width: 56px;
  height: 56px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 28px;
}

.logo-text h1 {
  font-size: 22px;
  color: #1A1F36;
  margin: 0 0 4px 0;
  font-weight: 700;
}

.logo-text p {
  font-size: 13px;
  color: #8A93B2;
  margin: 0;
}

/* 登录方式切换 */
.login-tabs {
  display: flex;
  gap: 8px;
  margin-bottom: 24px;
  background: #F0F2F8;
  padding: 4px;
  border-radius: 10px;
}

.login-tab {
  flex: 1;
  padding: 10px;
  text-align: center;
  font-size: 14px;
  font-weight: 600;
  color: #8A93B2;
  cursor: pointer;
  border-radius: 8px;
  transition: all 0.2s;
}

.login-tab.active {
  background: white;
  color: #667eea;
  box-shadow: 0 2px 8px rgba(102, 126, 234, 0.15);
}

/* 表单样式 */
.auth-form {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.admin-hint {
  background: linear-gradient(135deg, #FEF3C7 0%, #FDE68A 100%);
  border-radius: 10px;
  padding: 12px 16px;
  font-size: 12px;
  color: #92400E;
  line-height: 1.6;
}

.admin-hint strong {
  color: #B45309;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.form-label {
  font-size: 13px;
  font-weight: 600;
  color: #1A1F36;
}

.form-input {
  padding: 12px 16px;
  border: 1px solid #E4E7F0;
  border-radius: 10px;
  font-size: 14px;
  transition: all 0.2s;
  background: white;
}

.form-input:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.code-input-group {
  display: flex;
  gap: 10px;
}

.code-input-group .form-input {
  flex: 1;
}

.code-btn {
  padding: 0 16px;
  background: #F0F2F8;
  border: 1px solid #E4E7F0;
  border-radius: 10px;
  font-size: 13px;
  font-weight: 600;
  color: #667eea;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.2s;
}

.code-btn:hover:not(:disabled) {
  background: #667eea;
  color: white;
  border-color: #667eea;
}

.code-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.login-btn {
  padding: 14px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 10px;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  margin-top: 8px;
}

.login-btn:hover:not(:disabled) {
  transform: translateY(-1px);
  box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
}

.login-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
}

.form-error {
  color: #DC2626;
  font-size: 13px;
  text-align: center;
  padding: 10px;
  background: #FEE2E2;
  border-radius: 8px;
}

.form-links {
  text-align: center;
  font-size: 13px;
  color: #8A93B2;
  margin-top: 8px;
}

.form-links a {
  color: #667eea;
  text-decoration: none;
}

.form-links a:hover {
  text-decoration: underline;
}

.divider-line {
  margin: 0 10px;
  color: #E4E7F0;
}

/* 第三方登录 */
.social-login {
  margin-top: 24px;
  padding-top: 24px;
  border-top: 1px solid #E4E7F0;
}

.social-title {
  text-align: center;
  font-size: 12px;
  color: #8A93B2;
  margin-bottom: 16px;
}

.social-buttons {
  display: flex;
  justify-content: center;
  gap: 16px;
}

.social-btn {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  border: none;
  font-size: 24px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
}

.social-btn.wechat {
  background: #07c160;
}

.social-btn.wechat:hover {
  background: #06ad56;
  transform: scale(1.1);
}

.social-btn.qq {
  background: #12B7F5;
}

.social-btn.qq:hover {
  background: #0fa3db;
  transform: scale(1.1);
}

/* 协议勾选 */
.protocol-check {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-top: 20px;
  font-size: 12px;
  color: #8A93B2;
}

.protocol-check input[type="checkbox"] {
  width: 16px;
  height: 16px;
  cursor: pointer;
}

.protocol-check label {
  cursor: pointer;
}

.protocol-check a {
  color: #667eea;
  text-decoration: none;
}

.protocol-check a:hover {
  text-decoration: underline;
}
</style>
