<script setup lang="ts">
defineEmits<{
  (e: 'openModal', name: string): void
}>()

const emit = defineEmits<{
  (e: 'openModal', name: string): void
}>()
</script>

<template>
  <div class="topbar">
    <div class="breadcrumb">
      <span>格式转换工具</span>
      <span>›</span>
      <span class="current">工具大厅</span>
    </div>
    <div class="topbar-right">
      <button class="tb-btn ghost">📂 打开文件</button>
      <button class="tb-btn primary" @click="emit('openModal', '快速上传')">
        ⬆️ 上传转换
      </button>
      <div class="tb-icon" title="通知">🔔</div>
      <div class="tb-icon" title="帮助">❓</div>
    </div>
  </div>
</template>

<style scoped>
.topbar {
  height: 60px;
  background: var(--card);
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  padding: 0 28px;
  gap: 16px;
  flex-shrink: 0;
  box-shadow: 0 1px 0 var(--border);
}

.breadcrumb {
  font-size: 13px;
  color: var(--text-muted);
  display: flex;
  align-items: center;
  gap: 6px;
}

.breadcrumb .current {
  color: var(--text);
  font-weight: 700;
}

.topbar-right {
  margin-left: auto;
  display: flex;
  align-items: center;
  gap: 12px;
}

.tb-btn {
  padding: 7px 16px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  border: none;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: all 0.18s;
}

.tb-btn.primary {
  background: var(--primary);
  color: #fff;
}

.tb-btn.primary:hover {
  background: var(--primary-dark);
}

.tb-btn.ghost {
  background: var(--bg);
  color: var(--text);
  border: 1px solid var(--border);
}

.tb-btn.ghost:hover {
  background: var(--primary-light);
  border-color: var(--primary);
  color: var(--primary);
}

.tb-icon {
  width: 36px;
  height: 36px;
  border-radius: 8px;
  background: var(--bg);
  border: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 16px;
}
</style>