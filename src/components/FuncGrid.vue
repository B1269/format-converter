<script setup lang="ts">
import { funcBtnData } from '@/data'

const emit = defineEmits<{
  (e: 'openModal', name: string): void
}>()

const funcNameMap: Record<string, string> = {
  'image-content': '图片内容格式转换',
  'standard-doc': '标准文档格式转换',
  'custom-param': '设定参数格式转换',
  'word-pdf': 'Word转PDF',
  'pdf-word': 'PDF转Word',
  'image-pdf': '图片转PDF',
  'mp4-mp3': 'MP4转MP3',
  'pdf-merge': 'PDF自动合并'
}

function handleClick(funcId: string) {
  const modalName = funcNameMap[funcId]
  if (modalName) {
    emit('openModal', modalName)
  }
}
</script>

<template>
  <div class="panel">
    <div class="panel-header">
      <div class="panel-title">⚡ 快捷功能入口</div>
      <span class="panel-action">查看全部 ›</span>
    </div>
    <div class="panel-body">
      <div class="func-grid">
        <div
          v-for="func in funcBtnData"
          :key="func.id"
          :class="['func-btn', func.bgClass]"
          @click="handleClick(func.id)"
        >
          <span class="ficon">{{ func.icon }}</span>
          <span class="fname">{{ func.name }}</span>
          <span class="ftype">{{ func.type }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
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

.panel-body {
  padding: 16px 20px;
}

.func-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
}

.func-btn {
  border-radius: 12px;
  padding: 18px 10px 14px;
  text-align: center;
  cursor: pointer;
  transition: all 0.2s;
  border: 2px solid transparent;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.func-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 24px rgba(79, 110, 247, 0.14);
  border-color: var(--primary);
}

.func-btn .ficon {
  font-size: 30px;
}

.func-btn .fname {
  font-size: 12px;
  font-weight: 700;
  color: var(--text);
}

.func-btn .ftype {
  font-size: 11px;
  color: var(--text-muted);
}

.func-btn.bg1 {
  background: linear-gradient(135deg, rgba(79, 110, 247, 0.08), rgba(108, 142, 255, 0.12));
}

.func-btn.bg2 {
  background: linear-gradient(135deg, rgba(17, 153, 142, 0.08), rgba(56, 239, 125, 0.1));
}

.func-btn.bg3 {
  background: linear-gradient(135deg, rgba(245, 118, 76, 0.08), rgba(255, 210, 77, 0.1));
}

.func-btn.bg4 {
  background: linear-gradient(135deg, rgba(161, 140, 209, 0.1), rgba(251, 194, 235, 0.12));
}

.func-btn.bg5 {
  background: linear-gradient(135deg, rgba(79, 172, 254, 0.08), rgba(0, 242, 254, 0.1));
}

.func-btn.bg6 {
  background: linear-gradient(135deg, rgba(67, 206, 162, 0.08), rgba(24, 90, 157, 0.08));
}

.func-btn.bg7 {
  background: linear-gradient(135deg, rgba(255, 107, 107, 0.08), rgba(255, 217, 61, 0.1));
}

.func-btn.bg8 {
  background: linear-gradient(135deg, rgba(102, 126, 234, 0.08), rgba(118, 75, 162, 0.1));
}
</style>