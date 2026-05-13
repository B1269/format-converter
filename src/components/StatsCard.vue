<script setup lang="ts">
import { statsData } from '@/data'
</script>

<template>
  <div class="stats-row">
    <div
      v-for="stat in statsData"
      :key="stat.label"
      class="stat-card"
    >
      <div :class="['stat-icon', stat.color]">{{ stat.icon }}</div>
      <div>
        <div class="stat-num">{{ stat.value }}</div>
        <div class="stat-label">{{ stat.label }}</div>
        <div :class="['stat-change', stat.changeType]">{{ stat.change }}</div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.stats-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  margin-bottom: 24px;
}

.stat-card {
  background: var(--card);
  border-radius: var(--radius);
  padding: 20px 20px 18px;
  box-shadow: var(--shadow);
  display: flex;
  align-items: flex-start;
  gap: 14px;
  border: 1px solid var(--border);
  transition: transform 0.2s, box-shadow 0.2s;
}

.stat-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 30px rgba(79, 110, 247, 0.12);
}

.stat-icon {
  width: 46px;
  height: 46px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
  flex-shrink: 0;
}

.stat-icon.blue {
  background: linear-gradient(135deg, #4F6EF7, #6C8EFF);
}

.stat-icon.green {
  background: linear-gradient(135deg, #11998e, #38ef7d);
}

.stat-icon.orange {
  background: linear-gradient(135deg, #f7971e, #ffd200);
}

.stat-icon.purple {
  background: linear-gradient(135deg, #a18cd1, #fbc2eb);
}

.stat-num {
  font-size: 26px;
  font-weight: 800;
  color: var(--text);
  line-height: 1;
  margin-bottom: 4px;
}

.stat-label {
  font-size: 12px;
  color: var(--text-muted);
}

.stat-change {
  font-size: 11px;
  margin-top: 6px;
  display: flex;
  align-items: center;
  gap: 3px;
}

.stat-change.up {
  color: var(--success);
}

.stat-change.down {
  color: var(--danger);
}
</style>