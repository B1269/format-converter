<template>
  <div class="home-page">
    <!-- 左侧导航栏 -->
    <aside class="sidebar">
      <div class="logo-area">
        <div class="logo-title">
          <span>📄</span> 格式转换工具
        </div>
        <div class="logo-sub">Format Converter Pro</div>
      </div>

      <nav class="nav-section">
        <div class="nav-section-label">主要功能</div>
        <div :class="['nav-item', { active: currentPage === 'dashboard' }]" @click="currentPage = 'dashboard'">
          <span class="nav-icon">🏠</span><span>工具大厅</span>
        </div>
        <div :class="['nav-item', { active: currentPage === 'ai' }]" @click="currentPage = 'ai'">
          <span class="nav-icon">🤖</span><span>AI助手</span>
          <span class="nav-badge new">新</span>
        </div>
        <div :class="['nav-item', { active: currentPage === 'doc-convert' }]" @click="currentPage = 'doc-convert'">
          <span class="nav-icon">🔄</span><span>标准文档转换</span>
          <span class="nav-badge">7</span>
        </div>
        <div :class="['nav-item', { active: currentPage === 'image-recog' }]" @click="currentPage = 'image-recog'">
          <span class="nav-icon">🖼️</span><span>图片格式识别</span>
        </div>
        <div :class="['nav-item', { active: currentPage === 'param-convert' }]" @click="currentPage = 'param-convert'">
          <span class="nav-icon">⚙️</span><span>参数格式转换</span>
        </div>
      </nav>

      <nav class="nav-section">
        <div class="nav-section-label">文件操作</div>
        <div :class="['nav-item', { active: currentPage === 'word-pdf' }]" @click="currentPage = 'word-pdf'">
          <span class="nav-icon">📄</span><span>Word ↔ PDF</span>
        </div>
        <div :class="['nav-item', { active: currentPage === 'image-pdf' }]" @click="openModal('图片转PDF')">
          <span class="nav-icon">🖼️</span><span>图片 → PDF</span>
        </div>
        <div :class="['nav-item', { active: currentPage === 'mp4-mp3' }]" @click="openModal('MP4转MP3')">
          <span class="nav-icon">🎬</span><span>MP4 → MP3</span>
        </div>
        <div :class="['nav-item', { active: currentPage === 'pdf-merge' }]" @click="openModal('PDF自动合并')">
          <span class="nav-icon">🗂️</span><span>PDF 合并</span>
          <span class="nav-badge new">新</span>
        </div>
      </nav>

      <nav class="nav-section">
        <div class="nav-section-label">模版与工具</div>
        <div :class="['nav-item', { active: currentPage === 'templates' }]" @click="currentPage = 'templates'">
          <span class="nav-icon">📁</span><span>格式模版库</span>
        </div>
        <div :class="['nav-item', { active: currentPage === 'compress' }]" @click="openModal('视频高压缩')">
          <span class="nav-icon">🎞️</span><span>视频压缩</span>
        </div>
        <div :class="['nav-item', { active: currentPage === 'watermark' }]" @click="openModal('加水印')">
          <span class="nav-icon">💧</span><span>添加水印</span>
        </div>
      </nav>

      <nav class="nav-section">
        <div class="nav-section-label">账户</div>
        <div :class="['nav-item', { active: currentPage === 'history' }]" @click="currentPage = 'history'">
          <span class="nav-icon">🕐</span><span>历史记录</span>
        </div>
        <div :class="['nav-item', { active: currentPage === 'settings' }]" @click="currentPage = 'settings'">
          <span class="nav-icon">⚙️</span><span>系统设置</span>
        </div>
      </nav>

      <div class="sidebar-footer" @click="showUserPanel = !showUserPanel">
        <div class="avatar">{{ userAvatar }}</div>
        <div class="user-info">
          <div class="user-name">{{ userName }}</div>
          <div class="user-role">{{ userRole }}</div>
        </div>
        <div class="notif-dot"></div>
      </div>

      <!-- 用户面板 -->
      <div class="sidebar-user-panel" v-if="showUserPanel">
        <div class="panel-content">
          <div class="panel-avatar">{{ userAvatar }}</div>
          <div class="panel-name">{{ userName }}</div>
          <div class="panel-role">{{ userRole }}</div>
          <hr />
          <div class="panel-actions">
            <button class="panel-btn" @click="goToSettings">⚙️ 修改资料</button>
            <button class="panel-btn danger" @click="logout">🚪 退出登录</button>
          </div>
        </div>
      </div>
    </aside>

    <!-- 主内容区 -->
    <main class="main">
      <!-- 顶部栏 -->
      <header class="topbar">
        <div class="breadcrumb">
          <span class="current">{{ pageTitle }}</span>
        </div>
        <div class="topbar-right">
          <button class="tb-btn ghost" @click="openFile">📂 打开文件</button>
          <button class="tb-btn primary" @click="openModal('快速上传')">⬆️ 上传转换</button>
          <div class="tb-icon" title="通知">🔔</div>
          <div class="tb-icon" title="帮助">❓</div>
        </div>
      </header>

      <!-- 内容区 -->
      <div class="content">
        <!-- 工具大厅 -->
        <div v-if="currentPage === 'dashboard'">

          <!-- 统计卡片 -->
          <div class="stats-row">
            <div class="stat-card" v-for="stat in stats" :key="stat.label">
              <div :class="['stat-icon', stat.iconClass]">{{ stat.icon }}</div>
              <div>
                <div class="stat-num">{{ stat.value }}</div>
                <div class="stat-label">{{ stat.label }}</div>
                <div :class="['stat-change', stat.changeType]">{{ stat.change }}</div>
              </div>
            </div>
          </div>

          <div class="main-grid">
            <!-- 左侧列 -->
            <div class="left-column">
              <!-- 快捷功能入口 -->
              <div class="panel">
                <div class="panel-header">
                  <div class="panel-title">⚡ 快捷功能入口</div>
                  <span class="panel-action">查看全部 ›</span>
                </div>
                <div class="panel-body">
                  <div class="func-grid">
                    <div class="func-btn bg1" @click="openModal('图片内容格式转换')">
                      <span class="ficon">🖼️</span>
                      <span class="fname">图片格式识别</span>
                      <span class="ftype">智能提取字段</span>
                    </div>
                    <div class="func-btn bg2" @click="openModal('标准文档格式转换')">
                      <span class="ficon">📄</span>
                      <span class="fname">标准文档转换</span>
                      <span class="ftype">自动识别规范</span>
                    </div>
                    <div class="func-btn bg3" @click="openModal('设定参数格式转换')">
                      <span class="ficon">⚙️</span>
                      <span class="fname">自定义参数</span>
                      <span class="ftype">批量格式调整</span>
                    </div>
                    <div class="func-btn bg4" @click="openModal('Word转PDF')">
                      <span class="ficon">📝</span>
                      <span class="fname">Word → PDF</span>
                      <span class="ftype">.docx → .pdf</span>
                    </div>
                    <div class="func-btn bg5" @click="openModal('PDF转Word')">
                      <span class="ficon">📋</span>
                      <span class="fname">PDF → Word</span>
                      <span class="ftype">.pdf → .docx</span>
                    </div>
                    <div class="func-btn bg6" @click="openModal('图片转PDF')">
                      <span class="ficon">🖼️</span>
                      <span class="fname">图片 → PDF</span>
                      <span class="ftype">.jpg/.png → .pdf</span>
                    </div>
                    <div class="func-btn bg7" @click="openModal('MP4转MP3')">
                      <span class="ficon">🎬</span>
                      <span class="fname">MP4 → MP3</span>
                      <span class="ftype">提取音频</span>
                    </div>
                    <div class="func-btn bg8" @click="openModal('PDF自动合并')">
                      <span class="ficon">🗂️</span>
                      <span class="fname">PDF 合并</span>
                      <span class="ftype">自动/手动合并</span>
                    </div>
                  </div>
                </div>
              </div>

              <!-- 最近转换记录 -->
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
                    <tr v-for="(item, index) in recentHistory" :key="index">
                      <td>
                        <div class="file-name-cell">
                          <span class="file-icon">{{ item.icon }}</span>
                          <div class="file-text">
                            <div class="fn">{{ item.name }}</div>
                            <div class="fs">{{ item.type }}</div>
                          </div>
                        </div>
                      </td>
                      <td>{{ item.convertType }}</td>
                      <td>{{ item.size }}</td>
                      <td>{{ item.time }}</td>
                      <td>
                        <span :class="['status-badge', item.status]">{{ item.statusText }}</span>
                      </td>
                      <td>
                        <span class="action-link">{{ item.action }}</span>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            <!-- 右侧列 -->
            <div class="right-col">
              <!-- 热门模版 -->
              <div class="panel">
                <div class="panel-header">
                  <div class="panel-title">📁 热门模版</div>
                  <span class="panel-action">全部模版 ›</span>
                </div>
                <div class="template-list">
                  <div class="template-item" v-for="tpl in hotTemplates" :key="tpl.name" @click="openModal('合同模版')">
                    <span class="ti-icon">{{ tpl.icon }}</span>
                    <div class="ti-info">
                      <div class="ti-name">{{ tpl.name }}</div>
                      <div class="ti-desc">{{ tpl.desc }}</div>
                    </div>
                    <button class="ti-btn">下载</button>
                  </div>
                </div>
              </div>

              <!-- 其他实用工具 -->
              <div class="panel">
                <div class="panel-header">
                  <div class="panel-title">🛠️ 其他实用工具</div>
                </div>
                <div class="quick-ops">
                  <div class="quick-op-item" @click="openModal('视频高压缩')">
                    <span class="qop-icon">🎞️</span>
                    <div class="qop-text">
                      <div class="qop-name">视频高压缩</div>
                      <div class="qop-desc">H.265/AV1 高效压缩</div>
                    </div>
                    <span class="qop-arrow">›</span>
                  </div>
                  <div class="quick-op-item" @click="openModal('加水印')">
                    <span class="qop-icon">💧</span>
                    <div class="qop-text">
                      <div class="qop-name">添加水印</div>
                      <div class="qop-desc">图片/文档批量水印</div>
                    </div>
                    <span class="qop-arrow">›</span>
                  </div>
                  <div class="quick-op-item" @click="openModal('PDF自动合并')">
                    <span class="qop-icon">🗂️</span>
                    <div class="qop-text">
                      <div class="qop-name">PDF 自动合并</div>
                      <div class="qop-desc">多文档一键合并</div>
                    </div>
                    <span class="qop-arrow">›</span>
                  </div>
                  <div class="quick-op-item" @click="openModal('PDF手动合并')">
                    <span class="qop-icon">📑</span>
                    <div class="qop-text">
                      <div class="qop-name">PDF 手动合并</div>
                      <div class="qop-desc">可视化选页自定义合并</div>
                    </div>
                    <span class="qop-arrow">›</span>
                  </div>
                </div>
              </div>

              <!-- Pro升级卡 -->
              <div class="panel pro-card">
                <div class="panel-body">
                  <div style="font-size:20px;margin-bottom:8px;">💡</div>
                  <div class="pro-title">升级 Pro 版</div>
                  <div class="pro-desc">无限次转换 · 批量处理 · 优先队列 · 云端存储 30 天</div>
                  <button class="pro-btn">立即升级 →</button>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Word ↔ PDF 页面 -->
        <div v-else-if="currentPage === 'word-pdf'" class="word-pdf-content">
          <!-- 面包屑 -->
          <div class="wp-breadcrumb">
            <span class="wp-br-link" @click="currentPage = 'dashboard'">工具大厅</span>
            <span class="wp-br-sep">></span>
            <span class="wp-br-current">Word ↔ PDF</span>
          </div>

          <!-- 上部分：上传区域 -->
          <div class="wp-upload-section">
            <div
              class="wp-upload-area"
              :class="{ 'drag-over': wpDragging, 'has-file': wpHasFile }"
              @click="wpTriggerFile"
              @dragover.prevent="wpDragging = true"
              @dragleave.prevent="wpDragging = false"
              @drop.prevent="wpHandleDrop"
            >
              <input ref="wpFileInput" type="file" accept=".doc,.docx,.pdf" style="display:none" @change="wpHandleSelect" />

              <template v-if="!wpHasFile">
                <div class="wp-upload-icon">📁</div>
                <p class="wp-upload-title">拖拽文件到此处上传</p>
                <p class="wp-upload-hint">或点击选择文件</p>
                <div class="wp-format-tags">
                  <span class="wp-format-tag">.doc</span>
                  <span class="wp-format-tag">.docx</span>
                  <span class="wp-format-tag">.pdf</span>
                </div>
              </template>

              <template v-else>
                <div class="wp-uploaded">
                  <span class="wp-uploaded-icon">{{ wpUploadedIcon }}</span>
                  <div class="wp-uploaded-info">
                    <span class="wp-uploaded-name">{{ wpUploadedName }}</span>
                    <span class="wp-uploaded-size">{{ wpUploadedSize }}</span>
                  </div>
                  <button class="wp-btn-change" @click.stop="wpTriggerFile">更换文件</button>
                </div>
              </template>
            </div>

            <!-- 识别提示 -->
            <div v-if="wpDetectedFormat" class="wp-detect-hint">
              <span>🔍 检测到文件格式：</span>
              <strong>{{ wpDetectedFormat === 'pdf' ? 'PDF文档' : 'Word文档' }}</strong>
              <span class="wp-detect-arrow">→</span>
              <span>转换结果：</span>
              <strong>{{ wpDetectedFormat === 'pdf' ? 'Word文档' : 'PDF文档' }}</strong>
            </div>
          </div>

          <!-- 下部分：对比预览区域 -->
          <div class="wp-preview-section">
            <div class="wp-compare-view">
              <div class="wp-compare-container">
                <!-- 原文件预览 -->
                <div class="wp-compare-column">
                  <div class="wp-compare-header">
                    <span class="wp-compare-icon">{{ wpUploadedIcon }}</span>
                    <span class="wp-compare-title">原文件预览</span>
                  </div>
                  <div class="wp-compare-content">
                    <template v-if="wpHasFile">
                      <div class="wp-file-info">
                        <div class="wp-file-name">{{ wpUploadedName }}</div>
                        <div class="wp-file-size">{{ wpUploadedSize }}</div>
                        <div class="wp-file-format">{{ wpDetectedFormat === 'pdf' ? 'PDF文档' : 'Word文档' }}</div>
                      </div>
                      <div class="wp-preview-area">
                        <div class="wp-preview-text">{{ wpPreviewText }}</div>
                      </div>
                    </template>
                    <template v-else>
                      <div class="wp-preview-placeholder">
                        <div class="wp-preview-icon">📄</div>
                        <p>上传文件后显示预览</p>
                      </div>
                    </template>
                  </div>
                </div>
                
                <!-- 转换箭头 -->
                <div class="wp-compare-arrow">→</div>
                
                <!-- 转换结果预览 -->
                <div class="wp-compare-column">
                  <div class="wp-compare-header">
                    <span class="wp-compare-icon">{{ wpConvertedIcon || '🔄' }}</span>
                    <span class="wp-compare-title">转换预览</span>
                  </div>
                  <div class="wp-compare-content">
                    <template v-if="wpConvertedFile">
                      <div class="wp-file-info">
                        <div class="wp-file-name">{{ wpConvertedName }}</div>
                        <div class="wp-file-format">{{ wpDetectedFormat === 'pdf' ? 'Word文档' : 'PDF文档' }}</div>
                        <div class="wp-file-status success">✅ 转换完成</div>
                      </div>
                      <div class="wp-preview-area">
                        <div class="wp-preview-text">{{ wpConvertedText }}</div>
                      </div>
                    </template>
                    <template v-else>
                      <div class="wp-preview-placeholder">
                        <div class="wp-preview-icon">🔄</div>
                        <p>转换预览</p>
                        <p class="wp-preview-hint">点击"开始转换"后显示结果</p>
                      </div>
                    </template>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- 底部：操作按钮 -->
          <div class="wp-action-bar">
            <button class="wp-btn-convert" :disabled="!wpHasFile || wpConverting" @click="wpStartConvert">
              <span v-if="wpConverting" class="wp-spinner"></span>
              {{ wpConverting ? '转换中...' : '开始转换' }}
            </button>
            <button class="wp-btn-download" :disabled="!wpConvertedFile" @click="wpDownload">
              ↓ 下载文件
            </button>
          </div>

          <!-- 进度条 -->
          <div v-if="wpConverting" class="wp-progress">
            <div class="wp-progress-info">
              <span>正在转换...</span>
              <span>{{ wpProgress }}%</span>
            </div>
            <div class="wp-progress-track">
              <div class="wp-progress-fill" :style="{ width: wpProgress + '%' }"></div>
            </div>
          </div>
        </div>
      </div>
    </main>

    <!-- AI 悬浮按钮 -->
    <button class="ai-float-btn" @click="currentPage = 'ai'" title="AI助手">🤖</button>

    <!-- Modal 弹窗 -->
    <div class="modal-overlay" :class="{ show: showModal }" @click.self="closeModal">
      <div class="modal-box">
        <div class="modal-header">
          <div class="modal-title">{{ modalData.icon }}&nbsp;&nbsp;{{ modalData.name }}</div>
          <button class="modal-close" @click="closeModal">✕</button>
        </div>
        <div class="modal-body">
          <div class="modal-desc">{{ modalData.desc }}</div>
          
          <!-- 上传区域 - 支持拖拽 -->
          <div 
            v-if="modalData.uploadSub" 
            class="modal-upload" 
            :class="{ 'drag-over': isDragging }"
            @click="triggerFileInput"
            @dragover.prevent="isDragging = true"
            @dragleave.prevent="isDragging = false"
            @drop.prevent="handleDrop"
          >
            <input ref="fileInput" type="file" multiple hidden @change="handleFileSelect" />
            <div class="mu-icon">📂</div>
            <div class="mu-text">点击选择文件，或拖拽到此处</div>
            <div class="mu-sub">{{ modalData.uploadSub }}</div>
          </div>
          
          <!-- 已选择的文件列表 -->
          <div v-if="selectedFiles.length > 0" class="selected-files">
            <div class="sf-header">已选择文件：</div>
            <div class="sf-list">
              <div v-for="(file, index) in selectedFiles" :key="index" class="sf-item">
                <span class="sf-icon">{{ getFileIcon(file.name) }}</span>
                <span class="sf-name">{{ file.name }}</span>
                <span class="sf-size">{{ formatFileSize(file.size) }}</span>
                <span class="sf-remove" @click="removeFile(index)">✕</span>
              </div>
            </div>
          </div>
          
          <!-- 转换进度 -->
          <div v-if="isConverting" class="conversion-progress">
            <div class="cp-label">转换中...</div>
            <div class="cp-bar">
              <div class="cp-fill" :style="{ width: conversionProgress + '%' }"></div>
            </div>
            <div class="cp-percent">{{ conversionProgress }}%</div>
          </div>
          
          <!-- 参数选项 -->
          <div v-if="modalData.showParams">
            <div class="param-section">
              <div class="param-label">输出格式</div>
              <div class="param-chips">
                <div :class="['param-chip', { active: selectedQuality === '高质量' }]" @click="selectedQuality = '高质量'">高质量</div>
                <div :class="['param-chip', { active: selectedQuality === '标准' }]" @click="selectedQuality = '标准'">标准</div>
                <div :class="['param-chip', { active: selectedQuality === '小文件优先' }]" @click="selectedQuality = '小文件优先'">小文件优先</div>
              </div>
            </div>
            <div class="param-section">
              <div class="param-label">处理方式</div>
              <div class="param-chips">
                <div :class="['param-chip', { active: selectedMode === '自动识别' }]" @click="selectedMode = '自动识别'">自动识别</div>
                <div :class="['param-chip', { active: selectedMode === '手动配置' }]" @click="selectedMode = '手动配置'">手动配置</div>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button class="modal-btn cancel" @click="closeModal">取消</button>
          <button 
            class="modal-btn confirm" 
            @click="startConvert"
            :disabled="isConverting || selectedFiles.length === 0"
            :class="{ disabled: isConverting || selectedFiles.length === 0 }"
          >
            {{ isConverting ? '转换中...' : '🚀 开始转换' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_BASE = 'http://localhost:8000/api'

export default {
  name: 'HomePage',
  data() {
    return {
      currentPage: 'dashboard',
      showUserPanel: false,
      showModal: false,
      selectedQuality: '高质量',
      selectedMode: '自动识别',
      modalData: { icon: '', name: '', desc: '', uploadSub: '', showParams: false },
      selectedFiles: [],
      isConverting: false,
      conversionProgress: 0,
      isDragging: false,

      detailMap: {
        '图片内容格式转换': { icon:'🖼️', desc:'提取上传图片中的格式字段（一级标题、二级标题、三级标题、正文、表格、序号、引用、目录），识别后自动调整文档格式。界面对比显示原始内容与修改内容，修改处用红色字体标注，清晰直观。', uploadSub:'支持 JPG、PNG、BMP、TIFF 等图片格式', showParams: true },
        '标准文档格式转换': { icon:'📄', desc:'上传标准文档，自动识别其中的标题、目录、正文、序号、表格的字体格式，对需要修改的文档进行调整。调整界面并排显示原内容和修改内容，修改内容用红色字体清晰标注。', uploadSub:'支持 .docx .doc .wps', showParams: true },
        '设定参数格式转换': { icon:'⚙️', desc:'手动设定标题、目录、正文、序号、表格等各项字体格式参数，批量应用到上传的文档。调整预览界面同步显示原内容和修改后内容，修改部分红色标注。', uploadSub:'支持 .docx .doc .wps', showParams: true },
        'Word转PDF': { icon:'📝', desc:'将Word文档（.docx/.doc）一键转换为PDF格式，完整保留原有排版、字体、图表和页面布局，适合打印和分发。', uploadSub:'支持 .docx .doc .wps 格式', showParams: false },
        'PDF转Word': { icon:'📋', desc:'将PDF文件转换为可编辑的Word文档，智能识别文字、表格、图片，转换后可直接在Word中编辑修改。', uploadSub:'支持 .pdf 格式', showParams: false },
        '图片转PDF': { icon:'🖼️', desc:'将JPG/PNG等长图片文件转换为PDF文档，支持多张图片合并成一个PDF，方便打印和归档。', uploadSub:'支持 JPG、PNG，可多选', showParams: false },
        'MP4转MP3': { icon:'🎬', desc:'从MP4视频文件中提取音频轨道，转换为MP3格式，支持自定义音质和采样率。', uploadSub:'支持 .mp4 .avi .mov 格式', showParams: true },
        '合同模版': { icon:'📜', desc:'提供房屋租赁、采购、劳动、借款等常见合同的标准模版，符合法律规范，下载后可直接填写使用。', uploadSub:'', showParams: false },
        '视频高压缩': { icon:'🎞️', desc:'采用H.265、AV1等高压缩比编码算法，在保证画质的前提下大幅缩小视频文件体积，支持批量处理。', uploadSub:'支持 .mp4 .avi .mov .mkv', showParams: true },
        '加水印': { icon:'💧', desc:'支持为图片和文档批量添加文字水印，可自定义水印文本内容、字体大小、颜色、透明度、位置和角度。', uploadSub:'支持图片（JPG/PNG）和文档（docx/pdf）', showParams: true },
        'PDF自动合并': { icon:'🗂️', desc:'将多个PDF文档按照上传或拖拽排列的顺序自动合并成一个完整的PDF文件，一键完成。', uploadSub:'支持多选 .pdf 文件', showParams: false },
        'PDF手动合并': { icon:'📑', desc:'先分析各PDF文档的页面结构，拆分后可视化展示所有页面，手动勾选需要保留的页面并自定义合并顺序。', uploadSub:'支持多选 .pdf 文件', showParams: false },
        '快速上传': { icon:'⬆️', desc:'支持拖拽或点击上传，系统将自动识别文件类型并推荐最优转换方案，一站式完成上传与转换。', uploadSub:'支持 Word / PDF / 图片 / 视频 等全格式', showParams: false },
      },

      stats: [
        { icon: '🔄', iconClass: 'blue', value: '1,284', label: '累计转换次数', change: '↑ 12% 较上周', changeType: 'up' },
        { icon: '✅', iconClass: 'green', value: '98.7%', label: '转换成功率', change: '↑ 0.3%', changeType: 'up' },
        { icon: '📦', iconClass: 'orange', value: '3.2 GB', label: '累计处理文件', change: '↑ 230 MB 今日', changeType: 'up' },
        { icon: '⏱️', iconClass: 'purple', value: '1.8 s', label: '平均转换耗时', change: '↓ 0.2s 更快', changeType: 'down' },
      ],

      recentHistory: [
        { icon: '📄', name: '合同模板_2026.docx', type: 'Word文档', convertType: 'Word → PDF', size: '1.2 MB', time: '16:18', status: 'done', statusText: '✅ 完成', action: '下载' },
        { icon: '🖼️', name: '扫描件_001.jpg', type: 'JPEG图片', convertType: '图片 → PDF', size: '3.8 MB', time: '15:52', status: 'processing', statusText: '⏳ 处理中', action: '查看' },
        { icon: '🎬', name: '会议录音.mp4', type: 'MP4视频', convertType: 'MP4 → MP3', size: '128 MB', time: '14:30', status: 'done', statusText: '✅ 完成', action: '下载' },
        { icon: '📋', name: '年度报告.pdf', type: 'PDF文档', convertType: 'PDF → Word', size: '5.6 MB', time: '11:05', status: 'failed', statusText: '❌ 失败', action: '重试' },
        { icon: '📁', name: '论文初稿_v3.docx', type: 'Word文档', convertType: '格式规范转换', size: '2.1 MB', time: '09:44', status: 'done', statusText: '✅ 完成', action: '下载' },
      ],

      hotTemplates: [
        { icon: '📜', name: '房屋租赁合同', desc: '标准租房协议 · 即取即用' },
        { icon: '🏢', name: '采购合同模版', desc: '通用采购协议格式' },
        { icon: '🎓', name: '本科毕业论文', desc: '含封面/目录/正文格式' },
        { icon: '🎓', name: '硕士学位论文', desc: '研究生标准论文格式' },
        { icon: '📋', name: '会议纪要模版', desc: '规范会议记录格式' },
      ],

      // Word↔PDF 页面状态
      wpActiveTab: 'original', // 默认显示原文件预览，上传文件后也只能查看原文件预览
      wpPreviewTabs: [
        { id: 'compare', label: '对比预览' },
        { id: 'original', label: '原文件预览' },
        { id: 'converted', label: '转换预览' }
      ],
      wpDragging: false,
      wpHasFile: false,
      wpUploadedName: '',
      wpUploadedSize: '',
      wpUploadedIcon: '',
      wpDetectedFormat: '',
      wpPreviewText: '',
      wpConverting: false,
      wpProgress: 0,
      wpConvertedFile: null,
      wpConvertedName: '',
      wpConvertedIcon: '',
      wpConvertedText: '',
    }
  },

  computed: {
    pageTitle() {
      const map = {
        dashboard: '工具大厅',
        ai: 'AI助手',
        'doc-convert': '标准文档转换',
        'image-recog': '图片格式识别',
        'param-convert': '参数格式转换',
        'word-pdf': 'Word ↔ PDF',
        templates: '格式模版库',
        history: '历史记录',
        settings: '系统设置',
      }
      return map[this.currentPage] || '工具大厅'
    },
    userName() {
      const user = JSON.parse(localStorage.getItem('user') || '{}')
      return user.username || '用户'
    },
    userRole() {
      const user = JSON.parse(localStorage.getItem('user') || '{}')
      return user.role === 'admin' ? '👑 管理员' : '免费版 · 今日剩余 8 次'
    },
    userAvatar() {
      const avatars = ['👤', '👩', '👨', '👧', '👦', '👩‍💼', '👨‍💼', '🧑‍💼']
      return avatars[this.userName.length % avatars.length]
    },
  },

  methods: {
    openModal(name) {
      const d = this.detailMap[name] || { icon: '📄', desc: '功能描述', uploadSub: '', showParams: false }
      this.modalData = { ...d, name }
      this.selectedFiles = []
      this.isDragging = false
      this.showModal = true
    },
    closeModal() {
      this.showModal = false
      this.selectedFiles = []
      this.isConverting = false
      this.conversionProgress = 0
      this.isDragging = false
    },
    
    triggerFileInput() {
      this.$refs.fileInput?.click()
    },
    
    handleFileSelect(event) {
      const files = Array.from(event.target.files || [])
      this.addFiles(files)
    },
    
    handleDrop(event) {
      this.isDragging = false
      const files = Array.from(event.dataTransfer.files)
      this.addFiles(files)
    },
    
    addFiles(files) {
      if (files.length > 0) {
        this.selectedFiles = [...this.selectedFiles, ...files]
        this.modalData.uploadSub = `已选择 ${this.selectedFiles.length} 个文件`
      }
    },
    
    removeFile(index) {
      this.selectedFiles.splice(index, 1)
      if (this.selectedFiles.length === 0) {
        this.modalData.uploadSub = this.detailMap[this.modalData.name]?.uploadSub || ''
      } else {
        this.modalData.uploadSub = `已选择 ${this.selectedFiles.length} 个文件`
      }
    },
    
    getFileIcon(filename) {
      const ext = filename.split('.').pop().toLowerCase()
      const iconMap = {
        'pdf': '📋', 'doc': '📝', 'docx': '📝', 'wps': '📝',
        'jpg': '🖼️', 'jpeg': '🖼️', 'png': '🖼️', 'gif': '🖼️', 'bmp': '🖼️',
        'mp4': '🎬', 'avi': '🎬', 'mov': '🎬', 'mkv': '🎬',
        'mp3': '🎵', 'wav': '🎵', 'flac': '🎵',
      }
      return iconMap[ext] || '📄'
    },
    
    async startConvert() {
      if (this.selectedFiles.length === 0) {
        alert('请先选择文件')
        return
      }
      
      this.isConverting = true
      this.conversionProgress = 0
      
      const modalName = this.modalData.name
      
      try {
        let response
        const formData = new FormData()
        
        // 根据转换类型选择API
        if (modalName === 'Word转PDF') {
          formData.append('file', this.selectedFiles[0])
          response = await axios.post(`${API_BASE}/convert/word-to-pdf`, formData, {
            headers: { 'Content-Type': 'multipart/form-data' },
            responseType: 'blob',
            onUploadProgress: (e) => {
              this.conversionProgress = Math.round((e.loaded / e.total) * 90)
            }
          })
          this.downloadFile(response, this.selectedFiles[0].name.replace(/\.[^.]+$/, '.pdf'))
          
        } else if (modalName === 'PDF转Word') {
          formData.append('file', this.selectedFiles[0])
          response = await axios.post(`${API_BASE}/convert/pdf-to-word`, formData, {
            headers: { 'Content-Type': 'multipart/form-data' },
            responseType: 'blob',
            onUploadProgress: (e) => {
              this.conversionProgress = Math.round((e.loaded / e.total) * 90)
            }
          })
          this.downloadFile(response, this.selectedFiles[0].name.replace(/\.[^.]+$/, '.docx'))
          
        } else if (modalName === '图片转PDF') {
          this.selectedFiles.forEach(file => {
            formData.append('files', file)
          })
          response = await axios.post(`${API_BASE}/convert/image-to-pdf`, formData, {
            headers: { 'Content-Type': 'multipart/form-data' },
            responseType: 'blob',
            onUploadProgress: (e) => {
              this.conversionProgress = Math.round((e.loaded / e.total) * 90)
            }
          })
          this.downloadFile(response, 'converted.pdf')
          
        } else if (modalName === 'PDF自动合并') {
          this.selectedFiles.forEach(file => {
            formData.append('files', file)
          })
          response = await axios.post(`${API_BASE}/convert/pdf-merge`, formData, {
            headers: { 'Content-Type': 'multipart/form-data' },
            responseType: 'blob',
            onUploadProgress: (e) => {
              this.conversionProgress = Math.round((e.loaded / e.total) * 90)
            }
          })
          this.downloadFile(response, 'merged.pdf')
          
        } else if (modalName === 'MP4转MP3') {
          formData.append('file', this.selectedFiles[0])
          response = await axios.post(`${API_BASE}/convert/video-to-audio`, formData, {
            headers: { 'Content-Type': 'multipart/form-data' },
            responseType: 'blob',
            onUploadProgress: (e) => {
              this.conversionProgress = Math.round((e.loaded / e.total) * 90)
            }
          })
          this.downloadFile(response, this.selectedFiles[0].name.replace(/\.[^.]+$/, '.mp3'))
          
        } else {
          alert('该功能暂未开放，敬请期待！')
          this.closeModal()
          return
        }
        
        this.conversionProgress = 100
        
        // 成功后关闭弹窗
        setTimeout(() => {
          alert(`✅ 转换成功！文件已下载`)
          this.closeModal()
        }, 500)
        
      } catch (error) {
        console.error('转换失败:', error)
        if (error.response && error.response.data) {
          const reader = new FileReader()
          reader.onload = () => {
            try {
              const result = JSON.parse(reader.result)
              alert(`❌ 转换失败: ${result.detail || '未知错误'}`)
            } catch {
              alert('❌ 转换失败，请检查文件格式是否正确')
            }
          }
          reader.readAsText(error.response.data)
        } else {
          alert('❌ 转换失败，请确保后端服务已启动')
        }
        this.isConverting = false
        this.conversionProgress = 0
      }
    },
    
    downloadFile(response, defaultFilename) {
      const url = window.URL.createObjectURL(new Blob([response.data]))
      const link = document.createElement('a')
      link.href = url
      link.download = defaultFilename
      document.body.appendChild(link)
      link.click()
      document.body.removeChild(link)
      window.URL.revokeObjectURL(url)
    },
    
    openFile() {
      this.$refs.fileInput?.click()
    },
    goToSettings() {
      this.currentPage = 'settings'
      this.showUserPanel = false
    },
    formatFileSize(bytes) {
      if (bytes === 0) return '0 B'
      const k = 1024
      const sizes = ['B', 'KB', 'MB', 'GB']
      const i = Math.floor(Math.log(bytes) / Math.log(k))
      return parseFloat((bytes / Math.pow(k, i)).toFixed(1)) + ' ' + sizes[i]
    },
    logout() {
      if (confirm('确定要退出账户吗？')) {
        localStorage.removeItem('token')
        localStorage.removeItem('user')
        this.$router.push('/login')
      }
    },

    // Word↔PDF 方法
    wpHandleTab(tabId) {
      this.wpActiveTab = tabId
    },

    wpTriggerFile() {
      console.log('触发文件选择')
      const input = this.$refs.wpFileInput
      if (input) {
        input.value = '' // 清空之前的选择
        input.click()
      }
    },

    wpHandleSelect(event) {
      console.log('文件选择事件触发')
      const files = Array.from(event.target.files || [])
      console.log('选择的文件:', files)
      if (files.length > 0) {
        this.wpProcessFile(files[0])
      }
    },

    wpHandleDrop(event) {
      this.wpDragging = false
      const files = Array.from(event.dataTransfer.files)
      if (files.length > 0) {
        this.wpProcessFile(files[0])
      }
    },

    wpProcessFile(file) {
      console.log('处理文件:', file.name, '大小:', file.size)
      const ext = '.' + file.name.split('.').pop().toLowerCase()
      console.log('文件扩展名:', ext)

      if (!['.doc', '.docx', '.pdf'].includes(ext)) {
        alert('仅支持 .doc、.docx、.pdf 格式')
        return
      }

      this.wpUploadedName = file.name
      this.wpUploadedSize = this.formatFileSize(file.size)
      this.wpUploadedIcon = ext === '.pdf' ? '📋' : '📝'
      this.wpDetectedFormat = ext === '.pdf' ? 'pdf' : 'word'
      this.wpHasFile = true
      this.wpSelectedFile = file  // 保存文件对象
      console.log('wpHasFile 设置为 true')
      this.wpPreviewText = `文件：${file.name}\n大小：${this.wpUploadedSize}\n\n点击"原文件预览"查看详细内容`

      // 重置转换结果
      this.wpConvertedFile = null
      this.wpConvertedName = ''
      this.wpConvertedText = ''

      // 上传文件后只能查看原文件预览
      this.wpActiveTab = 'original'
    },

    wpStartConvert() {
      if (!this.wpHasFile || this.wpConverting) return

      this.wpConverting = true
      this.wpProgress = 0

      // 获取文件（优先使用保存的文件对象）
      const file = this.wpSelectedFile

      console.log('转换文件:', file?.name, file?.size)

      if (!file) {
        alert('请先选择文件')
        this.wpConverting = false
        return
      }

      // 模拟进度
      const timer = setInterval(() => {
        if (this.wpProgress < 85) {
          this.wpProgress += Math.random() * 15
          if (this.wpProgress > 85) this.wpProgress = 85
        }
      }, 200)

      // 构造FormData
      const formData = new FormData()
      formData.append('file', file)

      const endpoint = this.wpDetectedFormat === 'pdf'
        ? '/convert/pdf-to-word'
        : '/convert/word-to-pdf'

      console.log('请求API:', `${API_BASE}${endpoint}`)

      axios.post(`${API_BASE}${endpoint}`, formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
        responseType: 'blob'
      }).then(response => {
        clearInterval(timer)
        this.wpProgress = 100

        const ext = this.wpDetectedFormat === 'pdf' ? '.docx' : '.pdf'
        const baseName = this.wpUploadedName.replace(/\.[^.]+$/, '')
        this.wpConvertedName = baseName + ext
        this.wpConvertedIcon = this.wpDetectedFormat === 'pdf' ? '📝' : '📋'
        this.wpConvertedFile = response.data
        this.wpConvertedText = `转换成功！\n\n文件：${this.wpConvertedName}\n\n可以点击"转换预览"查看`

        alert('✅ 转换成功！')
        // 转换成功后自动切换到对比预览
        this.wpActiveTab = 'compare'

      }).catch(error => {
        clearInterval(timer)
        console.error('转换失败:', error)

        // 解析错误信息
        let errorMsg = '❌ 转换失败'
        if (error.response) {
          const status = error.response.status
          if (status === 500) {
            // 尝试读取后端返回的错误详情
            const reader = new FileReader()
            reader.onload = () => {
              try {
                const result = JSON.parse(reader.result)
                alert(`❌ 转换失败: ${result.detail || '服务器内部错误'}`)
              } catch {
                alert(`❌ 转换失败: 服务器内部错误（请检查后端日志）`)
              }
            }
            reader.readAsText(error.response.data)
            this.wpProgress = 0
            this.wpConverting = false
            return
          } else if (status === 400) {
            errorMsg = '❌ 文件格式不支持'
          } else {
            errorMsg = `❌ 转换失败，错误码: ${status}`
          }
        } else if (error.request) {
          errorMsg = '❌ 无法连接到后端服务，请检查：\n1. 后端是否已启动（python main.py）\n2. 端口是否正确（默认8000）'
        } else {
          errorMsg = `❌ 请求出错: ${error.message}`
        }
        alert(errorMsg)
        this.wpProgress = 0

      }).finally(() => {
        setTimeout(() => {
          this.wpConverting = false
        }, 500)
      })
    },

    wpDownload() {
      if (!this.wpConvertedFile) return

      const url = window.URL.createObjectURL(new Blob([this.wpConvertedFile]))
      const link = document.createElement('a')
      link.href = url
      link.download = this.wpConvertedName
      document.body.appendChild(link)
      link.click()
      document.body.removeChild(link)
      window.URL.revokeObjectURL(url)
    },
  },
}
</script>

<style scoped>
/* CSS 变量 */
.home-page {
  --primary: #4F6EF7;
  --primary-light: #EEF1FE;
  --primary-dark: #3451D1;
  --bg: #F0F2F8;
  --sidebar-bg: #1E2440;
  --sidebar-hover: #2A3258;
  --sidebar-active: #4F6EF7;
  --card: #FFFFFF;
  --text: #1A1F36;
  --text-muted: #8A93B2;
  --border: #E4E7F0;
  --success: #22C55E;
  --warning: #F59E0B;
  --danger: #EF4444;
  --shadow: 0 2px 16px rgba(79,110,247,0.08);
  --radius: 14px;

  display: flex;
  height: 100vh;
  overflow: hidden;
  font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Segoe UI", sans-serif;
  background: var(--bg);
  color: var(--text);
}

/* 侧边栏 */
.sidebar {
  width: 220px;
  background: var(--sidebar-bg);
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
  height: 100vh;
  overflow-y: auto;
}
.sidebar::-webkit-scrollbar { width: 0; }

.logo-area {
  padding: 24px 20px 20px;
  border-bottom: 1px solid rgba(255,255,255,0.07);
}
.logo-title { font-size: 17px; font-weight: 800; color: #fff; display: flex; align-items: center; gap: 8px; }
.logo-sub { font-size: 11px; color: rgba(255,255,255,0.4); margin-top: 4px; }

.nav-section { padding: 14px 0 4px; }
.nav-section-label {
  font-size: 10px; color: rgba(255,255,255,0.3);
  padding: 0 20px 6px;
  text-transform: uppercase; letter-spacing: 1.2px; font-weight: 700;
}
.nav-item {
  display: flex; align-items: center; gap: 10px;
  padding: 10px 20px;
  cursor: pointer;
  color: rgba(255,255,255,0.6);
  font-size: 13px; font-weight: 500;
  transition: all 0.18s;
  position: relative;
}
.nav-item:hover { background: var(--sidebar-hover); color: #fff; }
.nav-item.active { background: var(--sidebar-active); color: #fff; font-weight: 700; }
.nav-item.active::before {
  content: '';
  position: absolute; left: 0; top: 0; bottom: 0;
  width: 3px; background: #fff; border-radius: 0 2px 2px 0;
}
.nav-icon { font-size: 16px; flex-shrink: 0; }
.nav-badge {
  margin-left: auto;
  background: var(--primary);
  color: #fff; font-size: 10px; font-weight: 700;
  padding: 1px 6px; border-radius: 10px;
}
.nav-badge.new { background: var(--danger); }

.sidebar-footer {
  margin-top: auto;
  padding: 16px 20px;
  border-top: 1px solid rgba(255,255,255,0.07);
  display: flex; align-items: center; gap: 10px;
  cursor: pointer;
  transition: background 0.2s;
}
.sidebar-footer:hover { background: var(--sidebar-hover); }
.avatar { width: 32px; height: 32px; border-radius: 50%; background: linear-gradient(135deg,#4F6EF7,#9B59B6); display: flex; align-items: center; justify-content: center; font-size: 14px; flex-shrink: 0; }
.user-info { flex: 1; }
.user-name { font-size: 12px; color: #fff; font-weight: 600; }
.user-role { font-size: 10px; color: rgba(255,255,255,0.4); }
.notif-dot { width: 7px; height: 7px; border-radius: 50%; background: var(--danger); }

.sidebar-user-panel {
  background: var(--sidebar-bg);
  padding: 16px 20px;
  border-top: 1px solid rgba(255,255,255,0.07);
}
.panel-content { display: flex; flex-direction: column; align-items: center; }
.panel-avatar { width: 48px; height: 48px; border-radius: 50%; background: linear-gradient(135deg,#4F6EF7,#9B59B6); display: flex; align-items: center; justify-content: center; font-size: 22px; margin-bottom: 10px; }
.panel-name { font-size: 14px; font-weight: 700; color: #fff; margin-bottom: 5px; }
.panel-role { font-size: 11px; color: rgba(255,255,255,0.5); margin-bottom: 10px; }
.panel-content hr { width: 100%; border: none; border-top: 1px solid rgba(255,255,255,0.07); margin: 10px 0; }
.panel-actions { display: flex; flex-direction: column; gap: 8px; width: 100%; }
.panel-btn { width: 100%; padding: 8px; background: rgba(255,255,255,0.1); border: none; border-radius: 6px; color: #fff; font-size: 12px; cursor: pointer; transition: background 0.2s; }
.panel-btn:hover { background: rgba(255,255,255,0.2); }
.panel-btn.danger { background: rgba(239,68,68,0.2); }
.panel-btn.danger:hover { background: rgba(239,68,68,0.3); }

/* 主内容区 */
.main { flex: 1; display: flex; flex-direction: column; overflow: hidden; }

.topbar {
  height: 60px;
  background: var(--card);
  border-bottom: 1px solid var(--border);
  display: flex; align-items: center;
  padding: 0 28px;
  gap: 16px;
  flex-shrink: 0;
  box-shadow: 0 1px 0 var(--border);
}
.breadcrumb { font-size: 13px; color: var(--text-muted); display: flex; align-items: center; gap: 6px; }
.breadcrumb .current { color: var(--text); font-weight: 700; }
.topbar-right { margin-left: auto; display: flex; align-items: center; gap: 12px; }
.tb-btn {
  padding: 7px 16px; border-radius: 8px; font-size: 13px; font-weight: 600; cursor: pointer; border: none;
  display: flex; align-items: center; gap: 6px; transition: all 0.18s;
}
.tb-btn.primary { background: var(--primary); color: #fff; }
.tb-btn.primary:hover { background: var(--primary-dark); }
.tb-btn.ghost { background: var(--bg); color: var(--text); border: 1px solid var(--border); }
.tb-btn.ghost:hover { background: var(--primary-light); border-color: var(--primary); color: var(--primary); }
.tb-icon { width: 36px; height: 36px; border-radius: 8px; background: var(--bg); border: 1px solid var(--border); display: flex; align-items: center; justify-content: center; cursor: pointer; font-size: 16px; }

.content { flex: 1; overflow-y: auto; padding: 28px; }
.content::-webkit-scrollbar { width: 6px; }
.content::-webkit-scrollbar-track { background: transparent; }
.content::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }

/* 统计卡片 */
.stats-row { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 24px; }
.stat-card {
  background: var(--card);
  border-radius: var(--radius);
  padding: 20px 20px 18px;
  box-shadow: var(--shadow);
  display: flex; align-items: flex-start; gap: 14px;
  border: 1px solid var(--border);
  transition: transform 0.2s, box-shadow 0.2s;
}
.stat-card:hover { transform: translateY(-2px); box-shadow: 0 8px 30px rgba(79,110,247,0.12); }
.stat-icon { width: 46px; height: 46px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 22px; flex-shrink: 0; }
.stat-icon.blue { background: linear-gradient(135deg,#4F6EF7,#6C8EFF); }
.stat-icon.green { background: linear-gradient(135deg,#11998e,#38ef7d); }
.stat-icon.orange { background: linear-gradient(135deg,#f7971e,#ffd200); }
.stat-icon.purple { background: linear-gradient(135deg,#a18cd1,#fbc2eb); }
.stat-num { font-size: 26px; font-weight: 800; color: var(--text); line-height: 1; margin-bottom: 4px; }
.stat-label { font-size: 12px; color: var(--text-muted); }
.stat-change { font-size: 11px; margin-top: 6px; }
.stat-change.up { color: var(--success); }
.stat-change.down { color: var(--danger); }

/* 主网格 */
.main-grid { display: grid; grid-template-columns: 1fr 340px; gap: 20px; }
.left-column { display: flex; flex-direction: column; gap: 20px; }

/* 面板 */
.panel { background: var(--card); border-radius: var(--radius); box-shadow: var(--shadow); border: 1px solid var(--border); overflow: hidden; }
.panel-header { padding: 18px 20px 14px; border-bottom: 1px solid var(--border); display: flex; align-items: center; justify-content: space-between; }
.panel-title { font-size: 15px; font-weight: 700; display: flex; align-items: center; gap: 8px; }
.panel-action { font-size: 12px; color: var(--primary); cursor: pointer; font-weight: 600; }
.panel-action:hover { text-decoration: underline; }
.panel-body { padding: 16px 20px; }

/* 功能按钮网格 */
.func-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; }
.func-btn {
  border-radius: 12px;
  padding: 18px 10px 14px;
  text-align: center;
  cursor: pointer;
  transition: all 0.2s;
  border: 2px solid transparent;
  display: flex; flex-direction: column; align-items: center; gap: 8px;
}
.func-btn:hover { transform: translateY(-3px); box-shadow: 0 8px 24px rgba(79,110,247,0.14); border-color: var(--primary); }
.ficon { font-size: 30px; }
.fname { font-size: 12px; font-weight: 700; color: var(--text); }
.ftype { font-size: 11px; color: var(--text-muted); }
.func-btn.bg1 { background: linear-gradient(135deg,rgba(79,110,247,0.08),rgba(108,142,255,0.12)); }
.func-btn.bg2 { background: linear-gradient(135deg,rgba(17,153,142,0.08),rgba(56,239,125,0.1)); }
.func-btn.bg3 { background: linear-gradient(135deg,rgba(245,118,76,0.08),rgba(255,210,77,0.1)); }
.func-btn.bg4 { background: linear-gradient(135deg,rgba(161,140,209,0.1),rgba(251,194,235,0.12)); }
.func-btn.bg5 { background: linear-gradient(135deg,rgba(79,172,254,0.08),rgba(0,242,254,0.1)); }
.func-btn.bg6 { background: linear-gradient(135deg,rgba(67,206,162,0.08),rgba(24,90,157,0.08)); }
.func-btn.bg7 { background: linear-gradient(135deg,rgba(255,107,107,0.08),rgba(255,217,61,0.1)); }
.func-btn.bg8 { background: linear-gradient(135deg,rgba(102,126,234,0.08),rgba(118,75,162,0.1)); }

/* 文件表格 */
.file-table { width: 100%; border-collapse: collapse; }
.file-table th { font-size: 11px; color: var(--text-muted); font-weight: 600; text-align: left; padding: 8px 12px; background: var(--bg); border-bottom: 1px solid var(--border); }
.file-table td { padding: 12px 12px; font-size: 13px; border-bottom: 1px solid var(--border); vertical-align: middle; }
.file-table tr:last-child td { border-bottom: none; }
.file-table tr:hover td { background: var(--primary-light); }
.file-name-cell { display: flex; align-items: center; gap: 8px; }
.file-icon { font-size: 18px; }
.file-text .fn { font-weight: 600; font-size: 13px; color: var(--text); }
.file-text .fs { font-size: 11px; color: var(--text-muted); }
.status-badge { display: inline-flex; align-items: center; gap: 4px; padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 700; }
.status-badge.done { background: #DCFCE7; color: #15803D; }
.status-badge.processing { background: #FEF9C3; color: #A16207; }
.status-badge.failed { background: #FEE2E2; color: #B91C1C; }
.action-link { color: var(--primary); font-size: 12px; cursor: pointer; font-weight: 600; }
.action-link:hover { text-decoration: underline; }

/* 右侧列 */
.right-col { display: flex; flex-direction: column; gap: 20px; }

.template-list { display: flex; flex-direction: column; gap: 10px; padding: 0 20px 16px; }
.template-item {
  display: flex; align-items: center; gap: 12px;
  padding: 12px 14px;
  border-radius: 10px;
  background: var(--bg);
  cursor: pointer;
  border: 1px solid transparent;
  transition: all 0.18s;
}
.template-item:hover { background: var(--primary-light); border-color: var(--primary); }
.ti-icon { font-size: 24px; flex-shrink: 0; }
.ti-info { flex: 1; }
.ti-name { font-size: 13px; font-weight: 700; color: var(--text); }
.ti-desc { font-size: 11px; color: var(--text-muted); margin-top: 2px; }
.ti-btn { background: var(--primary-light); color: var(--primary); border: none; border-radius: 6px; padding: 5px 10px; font-size: 11px; font-weight: 700; cursor: pointer; }
.ti-btn:hover { background: var(--primary); color: #fff; }

.quick-ops { display: flex; flex-direction: column; gap: 8px; padding: 0 20px 16px; }
.quick-op-item {
  display: flex; align-items: center; gap: 12px;
  padding: 12px 14px;
  border-radius: 10px;
  cursor: pointer;
  border: 1px solid var(--border);
  background: var(--card);
  transition: all 0.18s;
}
.quick-op-item:hover { background: var(--primary-light); border-color: var(--primary); }
.qop-icon { font-size: 20px; flex-shrink: 0; }
.qop-text .qop-name { font-size: 13px; font-weight: 600; }
.qop-text .qop-desc { font-size: 11px; color: var(--text-muted); margin-top: 2px; }
.qop-arrow { margin-left: auto; color: var(--text-muted); }

/* Pro升级卡 */
.pro-card { background: linear-gradient(135deg, #4F6EF7, #6C8EFF) !important; border: none !important; }
.pro-title { font-size: 14px; font-weight: 800; color: #fff; margin-bottom: 6px; }
.pro-desc { font-size: 12px; color: rgba(255,255,255,0.85); line-height: 1.6; margin-bottom: 14px; }
.pro-btn { background: #fff; color: #4F6EF7; border: none; border-radius: 8px; padding: 9px 20px; font-size: 13px; font-weight: 800; cursor: pointer; width: 100%; }
.pro-btn:hover { opacity: 0.9; }

/* 占位页面 */
.placeholder-page { display: flex; flex-direction: column; align-items: center; justify-content: center; height: 50vh; color: var(--text-muted); }
.placeholder-icon { font-size: 64px; margin-bottom: 16px; }
.placeholder-text { font-size: 16px; }

/* AI 悬浮按钮 */
.ai-float-btn {
  position: fixed;
  bottom: 28px; right: 28px;
  width: 60px; height: 60px;
  border-radius: 50%;
  background: linear-gradient(135deg, #4F6EF7, #6C8EFF);
  border: none;
  cursor: pointer;
  font-size: 28px;
  display: flex; align-items: center; justify-content: center;
  box-shadow: 0 6px 24px rgba(79,110,247,0.4);
  transition: all 0.3s;
  z-index: 100;
}
.ai-float-btn:hover { transform: scale(1.1); box-shadow: 0 8px 32px rgba(79,110,247,0.5); }
.ai-float-btn::after {
  content: '';
  position: absolute;
  top: -4px; right: -4px;
  width: 16px; height: 16px;
  background: var(--danger);
  border-radius: 50%;
  border: 3px solid var(--bg);
}

/* Modal 弹窗 */
.modal-overlay {
  display: none;
  position: fixed; inset: 0;
  background: rgba(10,15,40,0.45);
  backdrop-filter: blur(3px);
  z-index: 1000;
  align-items: center; justify-content: center;
}
.modal-overlay.show { display: flex; }
.modal-box {
  background: var(--card);
  border-radius: 20px;
  width: 560px; max-width: 95vw;
  box-shadow: 0 24px 64px rgba(10,15,40,0.22);
  overflow: hidden;
  animation: modalIn 0.3s cubic-bezier(0.34,1.56,0.64,1);
}
@keyframes modalIn { from { transform: scale(0.88) translateY(20px); opacity:0; } to { transform: scale(1) translateY(0); opacity:1; } }
.modal-header { padding: 22px 24px 18px; border-bottom: 1px solid var(--border); display: flex; align-items: center; justify-content: space-between; }
.modal-title { font-size: 17px; font-weight: 800; display: flex; align-items: center; gap: 10px; }
.modal-close { width: 30px; height: 30px; border-radius: 8px; background: var(--bg); border: none; cursor: pointer; font-size: 16px; display: flex; align-items: center; justify-content: center; color: var(--text-muted); }
.modal-close:hover { background: var(--border); }
.modal-body { padding: 20px 24px; }
.modal-desc { font-size: 13px; color: var(--text-muted); line-height: 1.8; background: var(--bg); border-radius: 10px; padding: 14px 16px; margin-bottom: 18px; }
.modal-upload {
  border: 2px dashed var(--border);
  border-radius: 12px;
  padding: 28px;
  text-align: center;
  cursor: pointer;
  transition: all 0.2s;
  margin-bottom: 16px;
}
.modal-upload:hover { border-color: var(--primary); background: var(--primary-light); }
.modal-upload.drag-over { border-color: var(--primary); background: var(--primary-light); border-style: solid; }
.mu-icon { font-size: 36px; margin-bottom: 8px; }
.mu-text { font-size: 14px; font-weight: 600; color: var(--text); }
.mu-sub { font-size: 12px; color: var(--text-muted); margin-top: 4px; }
.modal-footer { padding: 0 24px 22px; display: flex; gap: 10px; justify-content: flex-end; }
.modal-btn { padding: 10px 24px; border-radius: 10px; font-size: 14px; font-weight: 700; cursor: pointer; border: none; transition: all 0.18s; }
.modal-btn.cancel { background: var(--bg); color: var(--text-muted); border: 1px solid var(--border); }
.modal-btn.cancel:hover { background: var(--border); }
.modal-btn.confirm { background: linear-gradient(135deg, var(--primary), #6C8EFF); color: #fff; }
.modal-btn.confirm:hover { box-shadow: 0 4px 14px rgba(79,110,247,0.35); }

.param-section { margin-bottom: 16px; }
.param-label { font-size: 12px; font-weight: 700; color: var(--text-muted); margin-bottom: 8px; }
.param-chips { display: flex; gap: 8px; flex-wrap: wrap; }
.param-chip { padding: 6px 14px; border-radius: 8px; font-size: 12px; font-weight: 600; cursor: pointer; border: 1px solid var(--border); background: var(--bg); color: var(--text-muted); transition: all 0.15s; }
.param-chip.active { background: var(--primary-light); border-color: var(--primary); color: var(--primary); }
.param-chip:hover { border-color: var(--primary); color: var(--primary); }

/* 已选择文件列表 */
.selected-files {
  background: var(--bg);
  border-radius: 10px;
  padding: 12px 16px;
  margin-bottom: 16px;
}
.sf-header { font-size: 12px; font-weight: 700; color: var(--text-muted); margin-bottom: 8px; }
.sf-list { display: flex; flex-direction: column; gap: 6px; max-height: 150px; overflow-y: auto; }
.sf-item {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 6px 10px;
  background: var(--card);
  border-radius: 6px;
  font-size: 12px;
}
.sf-icon { font-size: 14px; }
.sf-name { flex: 1; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; color: var(--text); }
.sf-size { color: var(--text-muted); font-size: 11px; }
.sf-remove { cursor: pointer; color: var(--text-muted); padding: 2px 6px; border-radius: 4px; }
.sf-remove:hover { background: var(--danger); color: #fff; }

/* 转换进度条 */
.conversion-progress {
  margin-top: 16px;
  padding: 14px 16px;
  background: var(--primary-light);
  border-radius: 10px;
}
.cp-label { font-size: 13px; font-weight: 600; color: var(--primary); margin-bottom: 10px; }
.cp-bar { height: 8px; background: rgba(79,110,247,0.2); border-radius: 4px; overflow: hidden; }
.cp-fill { height: 100%; background: linear-gradient(90deg, var(--primary), #6C8EFF); border-radius: 4px; transition: width 0.3s; }
.cp-percent { font-size: 12px; color: var(--primary); font-weight: 700; margin-top: 6px; text-align: right; }

/* ==================== Word↔PDF 页面样式 ==================== */
.word-pdf-content {
  padding: 24px;
  max-width: 900px;
  margin: 0 auto;
}

/* 面包屑 */
.wp-breadcrumb {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
  margin-bottom: 16px;
}
.wp-br-link { color: var(--text-muted); cursor: pointer; }
.wp-br-link:hover { color: var(--primary); }
.wp-br-sep { color: var(--text-muted); }
.wp-br-current { color: var(--text); font-weight: 600; }

/* 预览区域 */
.wp-preview-section {
  background: var(--card);
  border-radius: var(--radius);
  overflow: hidden;
  margin-bottom: 20px;
  box-shadow: var(--shadow);
}
.wp-preview-tabs {
  display: flex;
  border-bottom: 1px solid var(--border);
}
.wp-preview-tab {
  flex: 1;
  padding: 14px 20px;
  text-align: center;
  cursor: pointer;
  color: var(--text-muted);
  font-size: 14px;
  font-weight: 500;
  border-bottom: 2px solid transparent;
  transition: all 0.2s;
}
.wp-preview-tab:hover { color: var(--text); background: var(--bg); }
.wp-preview-tab.active { color: var(--primary); border-bottom-color: var(--primary); font-weight: 700; }
.wp-preview-body {
  min-height: 160px;
  padding: 20px;
}
.wp-preview-placeholder {
  height: 120px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: var(--bg);
  border-radius: 10px;
  color: var(--text-muted);
}
.wp-preview-icon { font-size: 32px; margin-bottom: 8px; }
.wp-preview-hint { font-size: 12px; margin-top: 4px; }

/* 文件预览 */
.wp-file-preview { }
.wp-file-header {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 14px;
  background: var(--bg);
  border-radius: 8px;
  margin-bottom: 12px;
}
.wp-file-icon { font-size: 22px; }
.wp-file-name { font-size: 14px; color: var(--text); }
.wp-file-content {
  padding: 14px;
  background: var(--bg);
  border-radius: 8px;
  max-height: 250px;
  overflow-y: auto;
}
.wp-preview-text {
  font-size: 13px;
  color: var(--text-muted);
  white-space: pre-wrap;
  line-height: 1.7;
}

/* 对比预览 */
.wp-compare-view {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 20px;
  height: 120px;
}
.wp-compare-box {
  flex: 1;
  max-width: 260px;
  padding: 16px;
  background: var(--bg);
  border-radius: 8px;
  text-align: center;
}
.wp-compare-label {
  font-size: 11px;
  color: var(--text-muted);
  margin-bottom: 10px;
}
.wp-compare-content {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  font-size: 13px;
  color: var(--text);
}
.wp-compare-arrow { font-size: 22px; color: var(--text-muted); }
.wp-pending { color: var(--text-muted); font-style: italic; }

/* 上传区域 */
.wp-upload-section { margin-bottom: 20px; }
.wp-upload-area {
  background: var(--card);
  border: 2px dashed var(--border);
  border-radius: var(--radius);
  padding: 28px;
  text-align: center;
  cursor: pointer;
  transition: all 0.2s;
}
.wp-upload-area:hover { border-color: var(--primary); }
.wp-upload-area.drag-over { border-color: var(--primary); background: var(--primary-light); border-style: solid; }
.wp-upload-area.has-file { border-style: solid; border-color: var(--border); }
.wp-upload-icon { font-size: 36px; margin-bottom: 10px; }
.wp-upload-title { font-size: 15px; font-weight: 600; color: var(--text); margin: 0 0 6px; }
.wp-upload-hint { font-size: 13px; color: var(--text-muted); margin: 0 0 14px; }
.wp-format-tags { display: flex; justify-content: center; gap: 8px; }
.wp-format-tag { padding: 4px 12px; background: var(--bg); border-radius: 4px; font-size: 12px; color: var(--text-muted); }

/* 已上传 */
.wp-uploaded {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 12px;
  background: var(--bg);
  border-radius: 8px;
}
.wp-uploaded-icon { font-size: 28px; }
.wp-uploaded-info { flex: 1; text-align: left; }
.wp-uploaded-name { display: block; font-size: 14px; color: var(--text); margin-bottom: 3px; }
.wp-uploaded-size { font-size: 12px; color: var(--text-muted); }
.wp-btn-change {
  padding: 8px 14px;
  border: 1px solid var(--border);
  border-radius: 6px;
  background: var(--card);
  color: var(--text-muted);
  font-size: 12px;
  cursor: pointer;
  transition: all 0.2s;
}
.wp-btn-change:hover { border-color: var(--primary); color: var(--primary); }

/* 识别提示 */
.wp-detect-hint {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  margin-top: 14px;
  padding: 10px;
  background: #E6F7FF;
  border-radius: 8px;
  font-size: 13px;
  color: var(--text);
}
.wp-detect-arrow { color: var(--text-muted); }

/* 操作栏 */
.wp-action-bar {
  display: flex;
  justify-content: center;
  gap: 14px;
  margin-bottom: 16px;
}
.wp-btn-back,
.wp-btn-convert,
.wp-btn-download {
  padding: 12px 24px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}
.wp-btn-back {
  border: 1px solid var(--border);
  background: var(--card);
  color: var(--text-muted);
}
.wp-btn-back:hover { background: var(--bg); }
.wp-btn-convert {
  flex: 1;
  max-width: 180px;
  border: none;
  background: var(--primary);
  color: #fff;
}
.wp-btn-convert:hover:not(:disabled) { background: var(--primary-dark); }
.wp-btn-download {
  border: 1px solid var(--primary);
  background: var(--card);
  color: var(--primary);
}
.wp-btn-download:hover:not(:disabled) { background: var(--primary-light); }
.wp-btn-convert:disabled,
.wp-btn-download:disabled {
  background: var(--bg);
  border-color: var(--border);
  color: var(--text-muted);
  cursor: not-allowed;
}
.wp-spinner {
  width: 14px;
  height: 14px;
  border: 2px solid rgba(255,255,255,0.3);
  border-top-color: #fff;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }

/* 进度条 */
.wp-progress {
  padding: 14px;
  background: var(--card);
  border-radius: 10px;
  margin-bottom: 20px;
}
.wp-progress-info {
  display: flex;
  justify-content: space-between;
  font-size: 13px;
  color: var(--text-muted);
  margin-bottom: 8px;
}
.wp-progress-track {
  height: 6px;
  background: var(--bg);
  border-radius: 3px;
  overflow: hidden;
}
.wp-progress-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--primary), #6C8EFF);
  border-radius: 3px;
  transition: width 0.3s ease;
}


/* 按钮禁用状态 */
.modal-btn.disabled { opacity: 0.5; cursor: not-allowed; }
.modal-btn.confirm:disabled { box-shadow: none; }

/* Word↔PDF 布局样式 - 上下分栏 */
.wp-upload-section {
  margin-bottom: 20px;
}
.wp-preview-section {
  margin-bottom: 20px;
}
.wp-action-bar {
  display: flex;
  justify-content: center;
  gap: 16px;
}

/* 新增预览样式 */
.wp-preview-header {
  padding: 20px 24px 16px;
  border-bottom: 1px solid var(--border);
}
.wp-preview-title {
  font-size: 16px;
  font-weight: 700;
  color: var(--text);
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 6px;
}
.wp-preview-icon {
  font-size: 22px;
}
.wp-preview-subtitle {
  font-size: 13px;
  color: var(--text-muted);
}
.wp-preview-content {
  padding: 24px;
}
.wp-file-details {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
  margin-bottom: 24px;
  padding: 16px;
  background: var(--bg);
  border-radius: 10px;
}
.wp-detail-item {
  display: flex;
  align-items: center;
}
.wp-detail-label {
  font-size: 13px;
  color: var(--text-muted);
  min-width: 80px;
}
.wp-detail-value {
  font-size: 13px;
  color: var(--text);
  font-weight: 500;
}
.wp-detail-value.success {
  color: var(--success);
}
.wp-preview-textarea {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 20px;
  margin-bottom: 20px;
  min-height: 120px;
  max-height: 200px;
  overflow-y: auto;
}
.wp-preview-text {
  font-size: 13px;
  line-height: 1.6;
  color: var(--text);
  white-space: pre-wrap;
}
.wp-preview-hint {
  display: flex;
  align-items: flex-start;
  gap: 8px;
  padding: 12px 16px;
  background: var(--primary-light);
  border-radius: 8px;
  font-size: 13px;
  color: var(--primary-dark);
}
.wp-preview-guide {
  margin-top: 16px;
  padding: 16px;
  background: var(--bg);
  border-radius: 10px;
  font-size: 13px;
}
.wp-preview-guide ol {
  margin: 8px 0 0 16px;
  padding: 0;
}
.wp-preview-guide li {
  margin-bottom: 6px;
  line-height: 1.5;
}

/* 对比预览样式 */
.wp-compare-container {
  display: flex;
  gap: 20px;
  padding: 20px;
}
.wp-compare-column {
  flex: 1;
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 12px;
  overflow: hidden;
}
.wp-compare-header {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 16px 20px;
  border-bottom: 1px solid var(--border);
  background: var(--bg);
}
.wp-compare-title {
  font-size: 15px;
  font-weight: 700;
  color: var(--text);
}
.wp-compare-content {
  padding: 20px;
}
.wp-file-info {
  margin-bottom: 20px;
  padding-bottom: 16px;
  border-bottom: 1px solid var(--border);
}
.wp-file-name {
  font-size: 14px;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 4px;
}
.wp-file-size, .wp-file-format, .wp-file-status {
  font-size: 12px;
  color: var(--text-muted);
  margin-bottom: 2px;
}
.wp-file-status.success {
  color: var(--success);
}
.wp-preview-area {
  background: var(--bg);
  border-radius: 8px;
  padding: 16px;
  min-height: 150px;
}
.wp-compare-arrow {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 28px;
  color: var(--primary);
  font-weight: 700;
  width: 40px;
}
</style>
