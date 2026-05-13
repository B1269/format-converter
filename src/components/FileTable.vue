<script setup lang="ts">
import { fileRecords } from '@/data'
</script>

<template>
  <div class="panel">
    <div class="panel-header">
      <div class="panel-title">🕐 最近转换记录</div>
      <span class="panel-action">查看全部 ›</span>
    </div>
    <table class="file-table">
      <thead>
        <tr>
          <th>文件名</th>
          <th>转换类型</th>
          <th>大小</th>
          <th>时间</th>
          <th>状态</th>
          <th>操作</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="file in fileRecords" :key="file.id">
          <td>
            <div class="file-name">
              <span class="file-icon">{{ file.icon }}</span>
              <div class="file-text">
                <div class="fn">{{ file.name }}</div>
                <div class="fs">{{ file.type }}</div>
              </div>
            </div>
          </td>
          <td>{{ file.convertType }}</td>
          <td>{{ file.size }}</td>
          <td>{{ file.time }}</td>
          <td>
            <span :class="['status-badge', file.status]">
              {{ file.status === 'done' ? '✅ 完成' : file.status === 'processing' ? '⏳ 处理中' : '❌ 失败' }}
            </span>
          </td>
          <td>
            <span class="action-link">{{ file.action }}</span>
          </td>
        </tr>
      </tbody>
    </table>
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

.file-table {
  width: 100%;
  border-collapse: collapse;
}

.file-table th {
  font-size: 11px;
  color: var(--text-muted);
  font-weight: 600;
  text-align: left;
  padding: 8px 12px;
  background: var(--bg);
  border-bottom: 1px solid var(--border);
}

.file-table td {
  padding: 12px 12px;
  font-size: 13px;
  border-bottom: 1px solid var(--border);
  vertical-align: middle;
}

.file-table tr:last-child td {
  border-bottom: none;
}

.file-table tr:hover td {
  background: var(--primary-light);
}

.file-name {
  display: flex;
  align-items: center;
  gap: 8px;
}

.file-icon {
  font-size: 18px;
}

.file-text .fn {
  font-weight: 600;
  font-size: 13px;
  color: var(--text);
}

.file-text .fs {
  font-size: 11px;
  color: var(--text-muted);
}

.status-badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 3px 10px;
  border-radius: 20px;
  font-size: 11px;
  font-weight: 700;
}

.status-badge.done {
  background: #DCFCE7;
  color: #15803D;
}

.status-badge.processing {
  background: #FEF9C3;
  color: #A16207;
}

.status-badge.failed {
  background: #FEE2E2;
  color: #B91C1C;
}

.action-link {
  color: var(--primary);
  font-size: 12px;
  cursor: pointer;
  font-weight: 600;
}

.action-link:hover {
  text-decoration: underline;
}
</style>