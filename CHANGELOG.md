# 格式化工场 (Format Converter) - 变更日志

## [v1.2] - 2026-05-15

### 新增
- Word ↔ PDF 双向转换功能
- 用户注册/登录系统（JWT认证）

### 优化
- Word转PDF页面改为上下分栏布局
  - 上：上传区域
  - 中：对比预览（原文件 | 转换结果）
  - 下：底部操作按钮

### 技术栈
- 前端：Vue3 + TypeScript + Vite
- 后端：FastAPI
- 数据库：SQLite

---

## v1.0 (初始版本)
- 基础前端框架搭建
- FastAPI 后端初始化
