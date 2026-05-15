<script setup lang="ts">
import { ref } from 'vue'
import Sidebar from '@/components/Sidebar.vue'
import Topbar from '@/components/Topbar.vue'
import StatsCard from '@/components/StatsCard.vue'
import FuncGrid from '@/components/FuncGrid.vue'
import FileTable from '@/components/FileTable.vue'
import RightPanel from '@/components/RightPanel.vue'
import Modal from '@/components/Modal.vue'

const modalVisible = ref(false)
const modalName = ref('')

function openModal(name: string) {
  modalName.value = name
  modalVisible.value = true
}

function closeModal() {
  modalVisible.value = false
}
</script>

<template>
  <div class="app-container">
    <Sidebar @open-modal="openModal" />
    <div class="main">
      <Topbar @open-modal="openModal" />
      <div class="content">
        <StatsCard />
        <div class="main-grid">
          <div class="left-col">
            <FuncGrid @open-modal="openModal" />
            <FileTable />
          </div>
          <RightPanel @open-modal="openModal" />
        </div>
      </div>
    </div>
    <Modal
      :visible="modalVisible"
      :modal-name="modalName"
      @close="closeModal"
    />
  </div>
</template>

<style scoped>
.app-container {
  display: flex;
  height: 100vh;
  overflow: hidden;
}

.main {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.content {
  flex: 1;
  overflow-y: auto;
  padding: 28px;
}

.content::-webkit-scrollbar {
  width: 6px;
}

.content::-webkit-scrollbar-track {
  background: transparent;
}

.content::-webkit-scrollbar-thumb {
  background: var(--border);
  border-radius: 3px;
}

.main-grid {
  display: grid;
  grid-template-columns: 1fr 340px;
  gap: 20px;
}

.left-col {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
</style>