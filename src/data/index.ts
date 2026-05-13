import type { NavSection, StatCardData, FuncBtnData, FileRecord, TemplateItem, QuickOpItem, ModalDetailMap } from '@/types'

export const navSections: NavSection[] = [
  {
    label: '主要功能',
    items: [
      { id: 'tools', icon: '🏠', label: '工具大厅' },
      { id: 'doc-convert', icon: '🔄', label: '标准文档转换', badge: '7' },
      { id: 'image-recog', icon: '🖼️', label: '图片格式识别' },
      { id: 'param-convert', icon: '⚙️', label: '参数格式转换' }
    ]
  },
  {
    label: '文件操作',
    items: [
      { id: 'word-pdf', icon: '📄', label: 'Word ↔ PDF' },
      { id: 'image-pdf', icon: '🖼️', label: '图片 → PDF' },
      { id: 'mp4-mp3', icon: '🎬', label: 'MP4 → MP3' },
      { id: 'pdf-merge', icon: '🗂️', label: 'PDF 合并', badge: '新', badgeType: 'new' }
    ]
  },
  {
    label: '模版与工具',
    items: [
      { id: 'templates', icon: '📁', label: '格式模版库' },
      { id: 'video-compress', icon: '🎞️', label: '视频压缩' },
      { id: 'watermark', icon: '💧', label: '添加水印' }
    ]
  },
  {
    label: '账户',
    items: [
      { id: 'history', icon: '🕐', label: '历史记录' },
      { id: 'settings', icon: '⚙️', label: '系统设置' }
    ]
  }
]

export const statsData: StatCardData[] = [
  {
    icon: '🔄',
    value: '1,284',
    label: '累计转换次数',
    change: '↑ 12% 较上周',
    changeType: 'up',
    color: 'blue'
  },
  {
    icon: '✅',
    value: '98.7%',
    label: '转换成功率',
    change: '↑ 0.3%',
    changeType: 'up',
    color: 'green'
  },
  {
    icon: '📦',
    value: '3.2 GB',
    label: '累计处理文件',
    change: '↑ 230 MB 今日',
    changeType: 'up',
    color: 'orange'
  },
  {
    icon: '⏱️',
    value: '1.8 s',
    label: '平均转换耗时',
    change: '↓ 0.2s 更快',
    changeType: 'down',
    color: 'purple'
  }
]

export const funcBtnData: FuncBtnData[] = [
  { id: 'image-content', icon: '🖼️', name: '图片格式识别', type: '智能提取字段', bgClass: 'bg1' },
  { id: 'standard-doc', icon: '📄', name: '标准文档转换', type: '自动识别规范', bgClass: 'bg2' },
  { id: 'custom-param', icon: '⚙️', name: '自定义参数', type: '批量格式调整', bgClass: 'bg3' },
  { id: 'word-pdf', icon: '📝', name: 'Word → PDF', type: '.docx → .pdf', bgClass: 'bg4' },
  { id: 'pdf-word', icon: '📋', name: 'PDF → Word', type: '.pdf → .docx', bgClass: 'bg5' },
  { id: 'image-pdf', icon: '🖼️', name: '图片 → PDF', type: '.jpg/.png → .pdf', bgClass: 'bg6' },
  { id: 'mp4-mp3', icon: '🎬', name: 'MP4 → MP3', type: '提取音频', bgClass: 'bg7' },
  { id: 'pdf-merge', icon: '🗂️', name: 'PDF 合并', type: '自动/手动合并', bgClass: 'bg8' }
]

export const fileRecords: FileRecord[] = [
  {
    id: '1',
    icon: '📄',
    name: '合同模板_2026.docx',
    type: 'Word文档',
    convertType: 'Word → PDF',
    size: '1.2 MB',
    time: '16:18',
    status: 'done',
    action: '下载'
  },
  {
    id: '2',
    icon: '🖼️',
    name: '扫描件_001.jpg',
    type: 'JPEG图片',
    convertType: '图片 → PDF',
    size: '3.8 MB',
    time: '15:52',
    status: 'processing',
    action: '查看'
  },
  {
    id: '3',
    icon: '🎬',
    name: '会议录音.mp4',
    type: 'MP4视频',
    convertType: 'MP4 → MP3',
    size: '128 MB',
    time: '14:30',
    status: 'done',
    action: '下载'
  },
  {
    id: '4',
    icon: '📋',
    name: '年度报告.pdf',
    type: 'PDF文档',
    convertType: 'PDF → Word',
    size: '5.6 MB',
    time: '11:05',
    status: 'failed',
    action: '重试'
  },
  {
    id: '5',
    icon: '📁',
    name: '论文初稿_v3.docx',
    type: 'Word文档',
    convertType: '格式规范转换',
    size: '2.1 MB',
    time: '09:44',
    status: 'done',
    action: '下载'
  }
]

export const templates: TemplateItem[] = [
  { id: '1', icon: '📜', name: '房屋租赁合同', desc: '标准租房协议 · 即取即用' },
  { id: '2', icon: '🏢', name: '采购合同模版', desc: '通用采购协议格式' },
  { id: '3', icon: '🎓', name: '本科毕业论文', desc: '含封面/目录/正文格式' },
  { id: '4', icon: '🎓', name: '硕士学位论文', desc: '研究生标准论文格式' },
  { id: '5', icon: '📋', name: '会议纪要模版', desc: '规范会议记录格式' }
]

export const quickOps: QuickOpItem[] = [
  { id: '1', icon: '🎞️', name: '视频高压缩', desc: 'H.265/AV1 高效压缩' },
  { id: '2', icon: '💧', name: '添加水印', desc: '图片/文档批量水印' },
  { id: '3', icon: '🗂️', name: 'PDF 自动合并', desc: '多文档一键合并' },
  { id: '4', icon: '📑', name: 'PDF 手动合并', desc: '可视化选页自定义合并' }
]

export const modalDetailMap: ModalDetailMap = {
  '图片内容格式转换': {
    icon: '🖼️',
    desc: '提取上传图片中的格式字段（一级标题、二级标题、三级标题、正文、表格、序号、引用、目录），识别后自动调整文档格式。界面对比显示原始内容与修改内容，修改处用红色字体标注，清晰直观。',
    uploadSub: '支持 JPG、PNG、BMP、TIFF 等图片格式',
    showParams: true
  },
  '标准文档格式转换': {
    icon: '📄',
    desc: '上传标准文档，自动识别其中的标题、目录、正文、序号、表格的字体格式，对需要修改的文档进行调整。调整界面并排显示原内容和修改内容，修改内容用红色字体清晰标注。',
    uploadSub: '支持 .docx .doc .wps',
    showParams: true
  },
  '设定参数格式转换': {
    icon: '⚙️',
    desc: '手动设定标题、目录、正文、序号、表格等各项字体格式参数，批量应用到上传的文档。调整预览界面同步显示原内容和修改后内容，修改部分红色标注。',
    uploadSub: '支持 .docx .doc .wps',
    showParams: true
  },
  'Word转PDF': {
    icon: '📝',
    desc: '将Word文档（.docx/.doc）一键转换为PDF格式，完整保留原有排版、字体、图表和页面布局，适合打印和分发。',
    uploadSub: '支持 .docx .doc .wps 格式',
    showParams: false
  },
  'PDF转Word': {
    icon: '📋',
    desc: '将PDF文件转换为可编辑的Word文档，智能识别文字、表格、图片，转换后可直接在Word中编辑修改。',
    uploadSub: '支持 .pdf 格式',
    showParams: false
  },
  '图片转PDF': {
    icon: '🖼️',
    desc: '将JPG/PNG等长图片文件转换为PDF文档，支持多张图片合并成一个PDF，方便打印和归档。',
    uploadSub: '支持 JPG、PNG，可多选',
    showParams: false
  },
  'MP4转MP3': {
    icon: '🎬',
    desc: '从MP4视频文件中提取音频轨道，转换为MP3格式，支持自定义音质和采样率。',
    uploadSub: '支持 .mp4 .avi .mov 格式',
    showParams: true
  },
  '合同模版': {
    icon: '📜',
    desc: '提供房屋租赁、采购、劳动、借款等常见合同的标准模版，符合法律规范，下载后可直接填写使用。',
    uploadSub: '',
    showParams: false
  },
  '毕业论文模版': {
    icon: '🎓',
    desc: '提供大学本科、硕士研究生、博士等不同学历层次的毕业论文格式模版，包含封面、目录、正文、参考文献等完整结构。',
    uploadSub: '',
    showParams: false
  },
  '会议标准模版': {
    icon: '📋',
    desc: '提供会议记录和会议纪要两种标准模版，包含议题、决议、参会人员、行动项等规范格式。',
    uploadSub: '',
    showParams: false
  },
  '视频高压缩': {
    icon: '🎞️',
    desc: '采用H.265、AV1等高压缩比编码算法，在保证画质的前提下大幅缩小视频文件体积，支持批量处理。',
    uploadSub: '支持 .mp4 .avi .mov .mkv',
    showParams: true
  },
  '加水印': {
    icon: '💧',
    desc: '支持为图片和文档批量添加文字水印，可自定义水印文本内容、字体大小、颜色、透明度、位置和角度。',
    uploadSub: '支持图片（JPG/PNG）和文档（docx/pdf）',
    showParams: true
  },
  'PDF自动合并': {
    icon: '🗂️',
    desc: '将多个PDF文档按照上传或拖拽排列的顺序自动合并成一个完整的PDF文件，一键完成。',
    uploadSub: '支持多选 .pdf 文件',
    showParams: false
  },
  'PDF手动合并': {
    icon: '📑',
    desc: '先分析各PDF文档的页面结构，拆分后可视化展示所有页面，手动勾选需要保留的页面并自定义合并顺序。',
    uploadSub: '支持多选 .pdf 文件',
    showParams: false
  },
  '快速上传': {
    icon: '⬆️',
    desc: '支持拖拽或点击上传，系统将自动识别文件类型并推荐最优转换方案，一站式完成上传与转换。',
    uploadSub: '支持 Word / PDF / 图片 / 视频 等全格式',
    showParams: false
  }
}