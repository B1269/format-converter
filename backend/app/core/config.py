"""
应用配置
"""
import os
from pathlib import Path

# 项目根目录
BASE_DIR = Path(__file__).parent.parent.parent
UPLOAD_DIR = BASE_DIR / "uploads"
OUTPUT_DIR = BASE_DIR / "outputs"

# 确保目录存在
UPLOAD_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

# 文件大小限制 (50MB)
MAX_FILE_SIZE = 50 * 1024 * 1024

# 支持的文件类型
SUPPORTED_CONVERSIONS = {
    "word_to_pdf": {
        "input": [".docx", ".doc"],
        "output": ".pdf",
        "description": "Word转PDF"
    },
    "excel_to_pdf": {
        "input": [".xlsx", ".xls"],
        "output": ".pdf",
        "description": "Excel转PDF"
    },
    "ppt_to_pdf": {
        "input": [".pptx", ".ppt"],
        "output": ".pdf",
        "description": "PPT转PDF"
    },
    "image_to_pdf": {
        "input": [".jpg", ".jpeg", ".png", ".bmp", ".gif"],
        "output": ".pdf",
        "description": "图片转PDF"
    },
    "pdf_merge": {
        "input": [".pdf"],
        "output": ".pdf",
        "description": "PDF合并"
    }
}

# 数据库配置
DATABASE_URL = "sqlite+aiosqlite:///./format_converter.db"
