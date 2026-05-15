const express = require('express');
const schedule = require('node-schedule');
const axios = require('axios');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 3000;

app.use(express.json());

const TEMPLATES_FILE = path.join(__dirname, 'templates.json');
const LOG_FILE = path.join(__dirname, 'sync.log');

let templates = [];

function loadTemplates() {
  try {
    if (fs.existsSync(TEMPLATES_FILE)) {
      const data = fs.readFileSync(TEMPLATES_FILE, 'utf8');
      templates = JSON.parse(data);
      console.log(`[${new Date().toISOString()}] 加载模板: ${templates.length} 个`);
    }
  } catch (err) {
    console.error('加载模板失败:', err);
    templates = [];
  }
}

function saveTemplates() {
  try {
    fs.writeFileSync(TEMPLATES_FILE, JSON.stringify(templates, null, 2), 'utf8');
    console.log(`[${new Date().toISOString()}] 保存模板成功: ${templates.length} 个`);
  } catch (err) {
    console.error('保存模板失败:', err);
  }
}

function log(message) {
  const logEntry = `[${new Date().toISOString()}] ${message}\n`;
  fs.appendFileSync(LOG_FILE, logEntry);
  console.log(logEntry.trim());
}

async function fetchTemplatesFromSource() {
  const sources = [
    {
      name: '高校模板库',
      url: 'https://api.example.com/templates/university',
      transform: (data) => data.map(t => ({
        id: t.id,
        category: '毕业论文',
        categoryType: 'thesis',
        name: t.title,
        desc: t.description,
        icon: '🎓',
        badge: t.isNew ? 'new' : (t.isHot ? 'hot' : ''),
        badgeText: t.isNew ? '新增' : (t.isHot ? '热门' : ''),
        format: '.docx',
        size: t.fileSize || '0 KB',
        downloads: t.downloadCount || '0',
        sections: t.chapters || [],
        source: 'university'
      }))
    },
    {
      name: '合同模板库',
      url: 'https://api.example.com/templates/contracts',
      transform: (data) => data.map(t => ({
        id: t.id,
        category: '合同模板',
        categoryType: 'contract',
        name: t.title,
        desc: t.description,
        icon: '📜',
        badge: t.isNew ? 'new' : (t.isHot ? 'hot' : ''),
        badgeText: t.isNew ? '新增' : (t.isHot ? '热门' : ''),
        format: '.docx',
        size: t.fileSize || '0 KB',
        downloads: t.downloadCount || '0',
        sections: t.chapters || [],
        source: 'contract'
      }))
    },
    {
      name: '会议纪要库',
      url: 'https://api.example.com/templates/meetings',
      transform: (data) => data.map(t => ({
        id: t.id,
        category: '会议纪要',
        categoryType: 'meeting',
        name: t.title,
        desc: t.description,
        icon: '📋',
        badge: t.isNew ? 'new' : (t.isHot ? 'hot' : ''),
        badgeText: t.isNew ? '新增' : (t.isHot ? '热门' : ''),
        format: '.docx',
        size: t.fileSize || '0 KB',
        downloads: t.downloadCount || '0',
        sections: t.chapters || [],
        source: 'meeting'
      }))
    }
  ];

  let allNewTemplates = [];

  for (const source of sources) {
    try {
      console.log(`正在从 ${source.name} 获取模板...`);
      const response = await axios.get(source.url, { timeout: 10000 });
      const transformed = source.transform(response.data);
      allNewTemplates = allNewTemplates.concat(transformed);
      log(`${source.name}: 获取到 ${transformed.length} 个模板`);
    } catch (err) {
      console.error(`${source.name} 获取失败:`, err.message);
      log(`${source.name} 获取失败: ${err.message}`);
    }
  }

  return allNewTemplates;
}

async function syncTemplates() {
  log('开始同步模板...');

  const newTemplates = await fetchTemplatesFromSource();

  const existingIds = new Set(templates.map(t => t.id));
  const newOnes = newTemplates.filter(t => !existingIds.has(t.id));

  if (newOnes.length > 0) {
    templates = templates.concat(newOnes);
    saveTemplates();
    log(`新增 ${newOnes.length} 个模板`);

    templates.forEach(t => {
      const newVersion = newTemplates.find(n => n.id === t.id);
      if (newVersion) {
        t.downloads = newVersion.downloads;
        t.size = newVersion.size;
      }
    });
    saveTemplates();
  } else {
    log('没有新增模板');
  }

  return {
    total: templates.length,
    new: newOnes.length,
    timestamp: new Date().toISOString()
  };
}

async function autoSyncDaily() {
  console.log('设置每日自动同步任务...');
  schedule.scheduleJob('0 8 * * *', async () => {
    console.log('执行每日自动同步...');
    await syncTemplates();
  });
  console.log('每日自动同步已设置: 每天 08:00 执行');
}

app.get('/api/templates', (req, res) => {
  const { category, search, page = 1, limit = 20 } = req.query;

  let filtered = [...templates];

  if (category && category !== 'all') {
    filtered = filtered.filter(t => t.categoryType === category);
  }

  if (search) {
    const keyword = search.toLowerCase();
    filtered = filtered.filter(t =>
      t.name.toLowerCase().includes(keyword) ||
      t.desc.toLowerCase().includes(keyword)
    );
  }

  const start = (page - 1) * limit;
  const end = start + parseInt(limit);
  const paginated = filtered.slice(start, end);

  res.json({
    success: true,
    data: {
      list: paginated,
      total: filtered.length,
      page: parseInt(page),
      limit: parseInt(limit),
      totalPages: Math.ceil(filtered.length / limit)
    }
  });
});

app.get('/api/templates/:id', (req, res) => {
  const template = templates.find(t => t.id === parseInt(req.params.id));

  if (!template) {
    return res.status(404).json({
      success: false,
      message: '模板不存在'
    });
  }

  res.json({
    success: true,
    data: template
  });
});

app.get('/api/templates/categories', (req, res) => {
  const categories = [
    { type: 'all', name: '全部模板', count: templates.length },
    { type: 'contract', name: '合同模板', count: templates.filter(t => t.categoryType === 'contract').length },
    { type: 'thesis', name: '毕业论文', count: templates.filter(t => t.categoryType === 'thesis').length },
    { type: 'meeting', name: '会议纪要', count: templates.filter(t => t.categoryType === 'meeting').length },
    { type: 'report', name: '工作报告', count: templates.filter(t => t.categoryType === 'report').length },
    { type: 'plan', name: '工作计划', count: templates.filter(t => t.categoryType === 'plan').length },
    { type: 'other', name: '其他模板', count: templates.filter(t => t.categoryType === 'other').length }
  ];

  res.json({
    success: true,
    data: categories
  });
});

app.post('/api/templates/sync', async (req, res) => {
  try {
    const result = await syncTemplates();
    res.json({
      success: true,
      message: '同步成功',
      data: result
    });
  } catch (err) {
    res.status(500).json({
      success: false,
      message: '同步失败',
      error: err.message
    });
  }
});

app.get('/api/templates/sync/status', (req, res) => {
  res.json({
    success: true,
    data: {
      lastSync: templates.length > 0 ? new Date().toISOString() : null,
      totalCount: templates.length,
      nextScheduledSync: '明天 08:00'
    }
  });
});

app.get('/api/health', (req, res) => {
  res.json({
    status: 'ok',
    timestamp: new Date().toISOString(),
    uptime: process.uptime()
  });
});

app.use((req, res) => {
  res.status(404).json({
    success: false,
    message: '接口不存在'
  });
});

loadTemplates();

app.listen(PORT, () => {
  console.log(`
╔═══════════════════════════════════════════════════════╗
║     模板自动更新接口服务                              ║
║     Template Auto-Update API Service                 ║
╠═══════════════════════════════════════════════════════╣
║  服务地址: http://localhost:${PORT}                     ║
║                                                       ║
║  接口列表:                                           ║
║  - GET  /api/templates         获取模板列表          ║
║  - GET  /api/templates/:id     获取模板详情          ║
║  - GET  /api/templates/categories  获取分类          ║
║  - POST /api/templates/sync     手动触发同步          ║
║  - GET  /api/templates/sync/status  同步状态         ║
║  - GET  /api/health             健康检查              ║
║                                                       ║
║  自动同步: 每天 08:00 自动从数据源更新模板            ║
╚═══════════════════════════════════════════════════════╝
  `);

  autoSyncDaily();
});