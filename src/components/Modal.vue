<script setup lang="ts">
import { ref, watch } from 'vue'
import { modalDetailMap } from '@/data'

const props = defineProps<{
  visible: boolean
  modalName: string
}>()

const emit = defineEmits<{
  (e: 'close'): void
}>()

const activeOutputChip = ref('高质量')
const activeProcessChip = ref('自动识别')

watch(() => props.visible, (newVal) => {
  if (newVal) {
    activeOutputChip.value = '高质量'
    activeProcessChip.value = '自动识别'
  }
})

const detail = () => modalDetailMap[props.modalName] || {
  icon: '📄',
  desc: '功能描述',
  uploadSub: '',
  showParams: false
}

function toggleChip(el: HTMLElement, group: 'output' | 'process') {
  const parent = el.closest('.param-chips')
  if (parent) {
    parent.querySelectorAll('.param-chip').forEach(c => c.classList.remove('active'))
    el.classList.add('active')
    if (group === 'output') {
      activeOutputChip.value = el.textContent || ''
    } else {
      activeProcessChip.value = el.textContent || ''
    }
  }
}

function handleOverlayClick(e: MouseEvent) {
  if ((e.target as HTMLElement).classList.contains('modal-overlay')) {
    emit('close')
  }
}

function handleKeydown(e: KeyboardEvent) {
  if (e.key === 'Escape') {
    emit('close')
  }
}
</script>

<template>
  <div
    :class="['modal-overlay', { show: visible }]"
    @click="handleOverlayClick"
    @keydown="handleKeydown"
  >
    <div class="modal-box">
      <div class="modal-header">
        <div class="modal-title">{{ detail().icon }} {{ modalName }}</div>
        <button class="modal-close" @click="emit('close')">✕</button>
      </div>
      <div class="modal-body">
        <div class="modal-desc">{{ detail().desc }}</div>

        <div
          v-if="detail().uploadSub"
          class="modal-upload"
        >
          <div class="mu-icon">📂</div>
          <div class="mu-text">点击选择文件，或拖拽到此处</div>
          <div class="mu-sub">{{ detail().uploadSub }}</div>
        </div>

        <div
          v-if="detail().showParams"
          id="modalParams"
        >
          <div class="param-section">
            <div class="param-label">输出格式</div>
            <div class="param-chips">
              <div
                :class="['param-chip', { active: activeOutputChip === '高质量' }]"
                @click="toggleChip($event.target as HTMLElement, 'output')"
              >
                高质量
              </div>
              <div
                :class="['param-chip', { active: activeOutputChip === '标准' }]"
                @click="toggleChip($event.target as HTMLElement, 'output')"
              >
                标准
              </div>
              <div
                :class="['param-chip', { active: activeOutputChip === '小文件优先' }]"
                @click="toggleChip($event.target as HTMLElement, 'output')"
              >
                小文件优先
              </div>
            </div>
          </div>
          <div class="param-section">
            <div class="param-label">处理方式</div>
            <div class="param-chips">
              <div
                :class="['param-chip', { active: activeProcessChip === '自动识别' }]"
                @click="toggleChip($event.target as HTMLElement, 'process')"
              >
                自动识别
              </div>
              <div
                :class="['param-chip', { active: activeProcessChip === '手动配置' }]"
                @click="toggleChip($event.target as HTMLElement, 'process')"
              >
                手动配置
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="modal-footer">
        <button class="modal-btn cancel" @click="emit('close')">取消</button>
        <button class="modal-btn confirm" @click="emit('close')">🚀 开始转换</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.modal-overlay {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(10, 15, 40, 0.45);
  backdrop-filter: blur(3px);
  z-index: 1000;
  align-items: center;
  justify-content: center;
}

.modal-overlay.show {
  display: flex;
}

.modal-box {
  background: var(--card);
  border-radius: 20px;
  width: 560px;
  max-width: 95vw;
  box-shadow: 0 24px 64px rgba(10, 15, 40, 0.22);
  overflow: hidden;
  animation: modalIn 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

@keyframes modalIn {
  from {
    transform: scale(0.88) translateY(20px);
    opacity: 0;
  }
  to {
    transform: scale(1) translateY(0);
    opacity: 1;
  }
}

.modal-header {
  padding: 22px 24px 18px;
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.modal-title {
  font-size: 17px;
  font-weight: 800;
  display: flex;
  align-items: center;
  gap: 10px;
}

.modal-close {
  width: 30px;
  height: 30px;
  border-radius: 8px;
  background: var(--bg);
  border: none;
  cursor: pointer;
  font-size: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-muted);
}

.modal-close:hover {
  background: var(--border);
}

.modal-body {
  padding: 20px 24px;
}

.modal-desc {
  font-size: 13px;
  color: var(--text-muted);
  line-height: 1.8;
  background: var(--bg);
  border-radius: 10px;
  padding: 14px 16px;
  margin-bottom: 18px;
}

.modal-upload {
  border: 2px dashed var(--border);
  border-radius: 12px;
  padding: 28px;
  text-align: center;
  cursor: pointer;
  transition: all 0.2s;
  margin-bottom: 16px;
}

.modal-upload:hover {
  border-color: var(--primary);
  background: var(--primary-light);
}

.modal-upload .mu-icon {
  font-size: 36px;
  margin-bottom: 8px;
}

.modal-upload .mu-text {
  font-size: 14px;
  font-weight: 600;
  color: var(--text);
}

.modal-upload .mu-sub {
  font-size: 12px;
  color: var(--text-muted);
  margin-top: 4px;
}

.modal-footer {
  padding: 0 24px 22px;
  display: flex;
  gap: 10px;
  justify-content: flex-end;
}

.modal-btn {
  padding: 10px 24px;
  border-radius: 10px;
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
  border: none;
  transition: all 0.18s;
}

.modal-btn.cancel {
  background: var(--bg);
  color: var(--text-muted);
  border: 1px solid var(--border);
}

.modal-btn.cancel:hover {
  background: var(--border);
}

.modal-btn.confirm {
  background: linear-gradient(135deg, var(--primary), #6C8EFF);
  color: #fff;
}

.modal-btn.confirm:hover {
  background: linear-gradient(135deg, var(--primary-dark), var(--primary));
  box-shadow: 0 4px 14px rgba(79, 110, 247, 0.35);
}

.param-section {
  margin-bottom: 16px;
}

.param-label {
  font-size: 12px;
  font-weight: 700;
  color: var(--text-muted);
  margin-bottom: 8px;
}

.param-chips {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.param-chip {
  padding: 6px 14px;
  border-radius: 8px;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  border: 1px solid var(--border);
  background: var(--bg);
  color: var(--text-muted);
  transition: all 0.15s;
}

.param-chip.active {
  background: var(--primary-light);
  border-color: var(--primary);
  color: var(--primary);
}

.param-chip:hover {
  border-color: var(--primary);
  color: var(--primary);
}
</style>