/**
 * API 服务
 */
const API_BASE_URL = 'http://localhost:8000/api'

interface ApiResponse<T = any> {
  success: boolean
  data?: T
  error?: string
}

/**
 * 认证API
 */
export const authApi = {
  /**
   * 用户注册
   */
  async register(username: string, email: string, password: string) {
    try {
      const response = await fetch(`${API_BASE_URL}/auth/register`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, email, password }),
      })

      const data = await response.json()

      if (response.ok) {
        return { success: true, user: data }
      } else {
        return { success: false, error: data.detail || '注册失败' }
      }
    } catch (error) {
      console.error('Register error:', error)
      return { success: false, error: '网络错误，请检查后端是否启动' }
    }
  },

  /**
   * 用户登录
   */
  async login(username: string, password: string) {
    try {
      const response = await fetch(`${API_BASE_URL}/auth/login`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      })

      const data = await response.json()

      if (response.ok) {
        // 获取用户信息
        const userResponse = await fetch(`${API_BASE_URL}/auth/me`, {
          headers: {
            'Authorization': `Bearer ${data.access_token}`,
          },
        })
        const userData = await userResponse.json()
        
        return { 
          success: true, 
          token: data.access_token,
          user: userData 
        }
      } else {
        return { success: false, error: data.detail || '登录失败' }
      }
    } catch (error) {
      console.error('Login error:', error)
      return { success: false, error: '网络错误，请检查后端是否启动' }
    }
  },

  /**
   * 获取当前用户信息
   */
  async getCurrentUser() {
    const token = localStorage.getItem('token')
    if (!token) return null

    try {
      const response = await fetch(`${API_BASE_URL}/auth/me`, {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      })

      if (response.ok) {
        return await response.json()
      }
      return null
    } catch (error) {
      console.error('Get user error:', error)
      return null
    }
  },

  /**
   * 检查是否已登录
   */
  isLoggedIn() {
    return !!localStorage.getItem('token')
  },

  /**
   * 退出登录
   */
  logout() {
    localStorage.removeItem('token')
    localStorage.removeItem('user')
  }
}

/**
 * 健康检查
 */
export async function healthCheck(): Promise<boolean> {
  try {
    const response = await fetch(`${API_BASE_URL}/health`)
    const data = await response.json()
    return data.status === 'healthy'
  } catch (error) {
    console.error('Health check failed:', error)
    return false
  }
}

/**
 * 获取支持的转换类型
 */
export async function getSupportedConversions() {
  try {
    const response = await fetch(`${API_BASE_URL}/supported-conversions`)
    return await response.json()
  } catch (error) {
    console.error('Get conversions failed:', error)
    return null
  }
}

/**
 * Word转PDF
 */
export async function convertWordToPdf(file: File): Promise<{ success: boolean; file?: File; error?: string }> {
  try {
    const formData = new FormData()
    formData.append('file', file)

    const response = await fetch(`${API_BASE_URL}/convert/word-to-pdf`, {
      method: 'POST',
      body: formData,
    })

    if (!response.ok) {
      const error = await response.json()
      return { success: false, error: error.detail || '转换失败' }
    }

    const contentDisposition = response.headers.get('content-disposition')
    let filename = 'converted.pdf'
    if (contentDisposition) {
      const match = contentDisposition.match(/filename[^;=\n]*=((['"]).*?\2|[^;\n]*)/)
      if (match) filename = match[1].replace(/['"]/g, '')
    }

    const blob = await response.blob()
    const convertedFile = new File([blob], filename, { type: 'application/pdf' })
    return { success: true, file: convertedFile }
  } catch (error) {
    console.error('Word to PDF conversion failed:', error)
    return { success: false, error: '转换服务不可用，请检查后端是否启动' }
  }
}

/**
 * 图片转PDF
 */
export async function convertImagesToPdf(files: File[]): Promise<{ success: boolean; file?: File; error?: string }> {
  try {
    const formData = new FormData()
    files.forEach((file) => {
      formData.append('files', file)
    })

    const response = await fetch(`${API_BASE_URL}/convert/image-to-pdf`, {
      method: 'POST',
      body: formData,
    })

    if (!response.ok) {
      const error = await response.json()
      return { success: false, error: error.detail || '转换失败' }
    }

    const blob = await response.blob()
    const convertedFile = new File([blob], 'converted.pdf', { type: 'application/pdf' })
    return { success: true, file: convertedFile }
  } catch (error) {
    console.error('Image to PDF conversion failed:', error)
    return { success: false, error: '转换服务不可用，请检查后端是否启动' }
  }
}

/**
 * PDF合并
 */
export async function mergePdfs(files: File[]): Promise<{ success: boolean; file?: File; error?: string }> {
  try {
    const formData = new FormData()
    files.forEach((file) => {
      formData.append('files', file)
    })

    const response = await fetch(`${API_BASE_URL}/convert/pdf-merge`, {
      method: 'POST',
      body: formData,
    })

    if (!response.ok) {
      const error = await response.json()
      return { success: false, error: error.detail || '合并失败' }
    }

    const blob = await response.blob()
    const mergedFile = new File([blob], 'merged.pdf', { type: 'application/pdf' })
    return { success: true, file: mergedFile }
  } catch (error) {
    console.error('PDF merge failed:', error)
    return { success: false, error: '合并服务不可用，请检查后端是否启动' }
  }
}

/**
 * 下载文件
 */
export function downloadFile(file: File) {
  const url = URL.createObjectURL(file)
  const a = document.createElement('a')
  a.href = url
  a.download = file.name
  document.body.appendChild(a)
  a.click()
  document.body.removeChild(a)
  URL.revokeObjectURL(url)
}
