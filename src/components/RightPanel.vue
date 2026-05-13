<script setup lang="ts">
import { templates, quickOps } from '@/data'

const emit = defineEmits<{
  (e: 'openModal', name: string): void
}>()

const templateModalMap: Record<string, string> = {
  '房屋租赁合同': '合同模版',
  '采购合同模版': '合同模版',
  '本科毕业论文': '毕业论文模版',
  '硕士学位论文': '毕业论文模版',
  '会议纪要模版': '会议标准模版'
}

const quickOpModalMap: Record<string, string> = {
  '视频高压缩': '视频高压缩',
  '添加水印': '加水印',
  'PDF 自动合并': 'PDF自动合并',
  'PDF 手动合并': 'PDF手动合并'
}

function handleTemplateClick(name: string) {
  const modalName = templateModalMap[name]
  if (modalName) {
    emit('openModal', modalName)
  }
}

function handleQuickOpClick(name: string) {
  const modalName = quickOpModalMap[name]
  if (modalName) {
    emit('openModal', modalName)
  }
}
</script>

<template>
  <div class="right-col">
    <div class="panel">
      <div class="panel-header">
        <div class="panel-title">📁 热门模版</div>
        <span class="panel-action">全部模版 ›</span>
      </div>
      <div class="template-list">
        <div
          v-for="template in templates"
          :key="template.id"
          class="template-item"
          @click="handleTemplateClick(template.name)"
        >
          <span class="ti-icon">{{ template.icon }}</span>
          <div class="ti-info">
            <div class="ti-name">{{ template.name }}</div>
            <div class="ti-desc">{{ template.desc }}</div>
          </div>
          <button class="ti-btn">下载</button>
        </div>
      </div>
    </div>

    <div class="panel">
      <div class="panel-header">
        <div class="panel-title">🛠️ 其他实用工具</div>
      </div>
      <div class="quick-ops">
        <div
          v-for="op in quickOps"
          :key="op.id"
          class="quick-op-item"
          @click="handleQuickOpClick(op.name)"
        >
          <span class="qop-icon">{{ op.icon }}</span>
          <div class="qop-text">
            <div class="qop-name">{{ op.name }}</div>
            <div class="qop-desc">{{ op.desc }}</div>
          </div>
          <span class="qop-arrow">›</span>
        </div>
      </div>
    </div>

    <div class="panel upgrade-panel">
      <div class="panel-body">
        <div class="upgrade-icon">💡</div>
        <div class="upgrade-title">升级 Pro 版</div>
        <div class="upgrade-desc">无限次转换 · 批量处理 · 优先队列 · 云端存储 30 天</div>
        <button class="upgrade-btn">立即升级 →</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.right-col {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.panel {
  background: var(--card);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  border: 1px solid var(--border);
  overflow: hidden;
}

.panel-header {
  padding: 18px 20px 14px;
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.panel-title {
  font-size: 15px;
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 8px;
}

.panel-action {
  font-size: 12px;
  color: var(--primary);
  cursor: pointer;
  font-weight: 600;
}

.panel-action:hover {
  text-decoration: underline;
}

.template-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding: 0 20px 16px;
}

.template-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 14px;
  border-radius: 10px;
  background: var(--bg);
  cursor: pointer;
  border: 1px solid transparent;
  transition: all 0.18s;
}

.template-item:hover {
  background: var(--primary-light);
  border-color: var(--primary);
}

.template-item .ti-icon {
  font-size: 24px;
  flex-shrink: 0;
}

.template-item .ti-info {
  flex: 1;
}

.template-item .ti-name {
  font-size: 13px;
  font-weight: 700;
  color: var(--text);
}

.template-item .ti-desc {
  font-size: 11px;
  color: var(--text-muted);
  margin-top: 2px;
}

.template-item .ti-btn {
  background: var(--primary-light);
  color: var(--primary);
  border: none;
  border-radius: 6px;
  padding: 5px 10px;
  font-size: 11px;
  font-weight: 700;
  cursor: pointer;
}

.template-item .ti-btn:hover {
  background: var(--primary);
  color: #fff;
}

.quick-ops {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 0 20px 16px;
}

.quick-op-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 14px;
  border-radius: 10px;
  cursor: pointer;
  border: 1px solid var(--border);
  background: var(--card);
  transition: all 0.18s;
}

.quick-op-item:hover {
  background: var(--primary-light);
  border-color: var(--primary);
}

.qop-icon {
  font-size: 20px;
  flex-shrink: 0;
}

.qop-text .qop-name {
  font-size: 13px;
  font-weight: 600;
}

.qop-text .qop-desc {
  font-size: 11px;
  color: var(--text-muted);
  margin-top: 2px;
}

.qop-arrow {
  margin-left: auto;
  color: var(--text-muted);
}

.upgrade-panel {
  background: linear-gradient(135deg, #4F6EF7, #6C8EFF);
  border: none;
}

.upgrade-panel .panel-body {
  color: #fff;
  padding: 20px;
}

.upgrade-icon {
  font-size: 20px;
  margin-bottom: 8px;
}

.upgrade-title {
  font-size: 14px;
  font-weight: 800;
  margin-bottom: 6px;
}

.upgrade-desc {
  font-size: 12px;
  opacity: 0.85;
  line-height: 1.6;
  margin-bottom: 14px;
}

.upgrade-btn {
  background: #fff;
  color: #4F6EF7;
  border: none;
  border-radius: 8px;
  padding: 9px 20px;
  font-size: 13px;
  font-weight: 800;
  cursor: pointer;
  width: 100%;
}
</style>