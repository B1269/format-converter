export interface NavItem {
  id: string
  icon: string
  label: string
  badge?: string
  badgeType?: 'normal' | 'new'
}

export interface NavSection {
  label: string
  items: NavItem[]
}

export interface StatCardData {
  icon: string
  value: string
  label: string
  change: string
  changeType: 'up' | 'down'
  color: 'blue' | 'green' | 'orange' | 'purple'
}

export interface FuncBtnData {
  id: string
  icon: string
  name: string
  type: string
  bgClass: string
}

export interface FileRecord {
  id: string
  icon: string
  name: string
  type: string
  convertType: string
  size: string
  time: string
  status: 'done' | 'processing' | 'failed'
  action: string
}

export interface TemplateItem {
  id: string
  icon: string
  name: string
  desc: string
}

export interface QuickOpItem {
  id: string
  icon: string
  name: string
  desc: string
}

export interface ModalDetail {
  icon: string
  desc: string
  uploadSub: string
  showParams: boolean
}

export interface ModalDetailMap {
  [key: string]: ModalDetail
}