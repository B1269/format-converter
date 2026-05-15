<script setup lang="ts">
import { ref } from 'vue'
import { navSections } from '@/data'

defineEmits<{
  (e: 'openModal', name: string): void
}>()

const emit = defineEmits<{
  (e: 'openModal', name: string): void
}>()

const activeNav = ref('tools')

const navClickMap: Record<string, string> = {
  'image-recog': '图片内容格式转换',
  'param-convert': '设定参数格式转换',
  'doc-convert': '标准文档格式转换'
}

function handleNavClick(itemId: string, itemLabel: string) {
  activeNav.value = itemId
  const modalName = navClickMap[itemId]
  if (modalName) {
    emit('openModal', modalName)
  }
}
</script>

<template>
  <div class="sidebar">
    <div class="logo-area">
      <div class="logo-title">📄 格式转换工具</div>
      <div class="logo-sub">Format Converter Pro</div>
    </div>

    <div
      v-for="section in navSections"
      :key="section.label"
      class="nav-section"
    >
      <div class="nav-section-label">{{ section.label }}</div>
      <div
        v-for="item in section.items"
        :key="item.id"
        :class="['nav-item', { active: activeNav === item.id }]"
        @click="handleNavClick(item.id, item.label)"
      >
        <span class="nav-icon">{{ item.icon }}</span>
        {{ item.label }}
        <span
          v-if="item.badge"
          :class="['nav-badge', { new: item.badgeType === 'new' }]"
        >
          {{ item.badge }}
        </span>
      </div>
    </div>

    <div class="sidebar-footer">
      <div class="avatar">👤</div>
      <div class="user-info">
        <div class="user-name">管理员</div>
        <div class="user-role">免费版 · 今日剩余 8 次</div>
      </div>
      <div class="notif-dot"></div>
    </div>
  </div>
</template>

<style scoped>
.sidebar {
  width: 220px;
  background: var(--sidebar-bg);
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
  height: 100vh;
  overflow-y: auto;
}

.sidebar::-webkit-scrollbar {
  width: 0;
}

.logo-area {
  padding: 24px 20px 20px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.07);
}

.logo-title {
  font-size: 17px;
  font-weight: 800;
  color: #fff;
  display: flex;
  align-items: center;
  gap: 8px;
}

.logo-sub {
  font-size: 11px;
  color: rgba(255, 255, 255, 0.4);
  margin-top: 4px;
}

.nav-section {
  padding: 14px 0 4px;
}

.nav-section-label {
  font-size: 10px;
  color: rgba(255, 255, 255, 0.3);
  padding: 0 20px 6px;
  text-transform: uppercase;
  letter-spacing: 1.2px;
  font-weight: 700;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 20px;
  cursor: pointer;
  border-radius: 0;
  color: rgba(255, 255, 255, 0.6);
  font-size: 13px;
  font-weight: 500;
  transition: all 0.18s;
  position: relative;
}

.nav-item:hover {
  background: var(--sidebar-hover);
  color: #fff;
}

.nav-item.active {
  background: var(--sidebar-active);
  color: #fff;
  font-weight: 700;
}

.nav-item.active::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 3px;
  background: #fff;
  border-radius: 0 2px 2px 0;
}

.nav-icon {
  font-size: 16px;
  flex-shrink: 0;
}

.nav-badge {
  margin-left: auto;
  background: var(--primary);
  color: #fff;
  font-size: 10px;
  font-weight: 700;
  padding: 1px 6px;
  border-radius: 10px;
}

.nav-badge.new {
  background: var(--danger);
}

.sidebar-footer {
  margin-top: auto;
  padding: 16px 20px;
  border-top: 1px solid rgba(255, 255, 255, 0.07);
  display: flex;
  align-items: center;
  gap: 10px;
}

.avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: linear-gradient(135deg, #4F6EF7, #9B59B6);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  flex-shrink: 0;
}

.user-info {
  flex: 1;
}

.user-name {
  font-size: 12px;
  color: #fff;
  font-weight: 600;
}

.user-role {
  font-size: 10px;
  color: rgba(255, 255, 255, 0.4);
}

.notif-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--danger);
  display: inline-block;
}
</style>