"""
文件转换服务
"""
import os
import uuid
from pathlib import Path
from typing import Optional
from fastapi import UploadFile

from app.core.config import UPLOAD_DIR, OUTPUT_DIR, SUPPORTED_CONVERSIONS


class ConversionService:
    """转换服务"""

    @staticmethod
    async def save_upload_file(upload_file: UploadFile) -> str:
        """保存上传文件，返回文件路径"""
        # 生成唯一文件名
        ext = Path(upload_file.filename).suffix
        unique_name = f"{uuid.uuid4().hex}{ext}"
        file_path = UPLOAD_DIR / unique_name

        # 写入文件
        content = await upload_file.read()
        with open(file_path, "wb") as f:
            f.write(content)

        return str(file_path)

    @staticmethod
    def word_to_pdf(input_path: str) -> str:
        """
        Word转PDF
        使用python-docx处理.docx文件
        对于.doc文件需要LibreOffice支持
        """
        from docx import Document

        input_file = Path(input_path)
        output_file = OUTPUT_DIR / f"{input_file.stem}.pdf"

        # 读取Word文档
        doc = Document(input_path)

        # 转换为PDF（简化实现，实际需要用LibreOffice或专门的库）
        # 这里我们创建一个简单的处理流程
        try:
            # 使用reportlab创建PDF
            from reportlab.lib.pagesizes import A4
            from reportlab.lib.styles import getSampleStyleSheet
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
            from reportlab.lib.units import cm

            doc_pdf = SimpleDocTemplate(
                str(output_file),
                pagesize=A4,
                rightMargin=2*cm,
                leftMargin=2*cm,
                topMargin=2*cm,
                bottomMargin=2*cm
            )

            styles = getSampleStyleSheet()
            story = []

            # 转换段落
            for para in doc.paragraphs:
                if para.text.strip():
                    story.append(Paragraph(para.text, styles['Normal']))
                    story.append(Spacer(1, 12))

            # 转换表格
            for table in doc.tables:
                for row in table.rows:
                    row_text = " | ".join([cell.text for cell in row.cells])
                    story.append(Paragraph(row_text, styles['Normal']))
                story.append(Spacer(1, 12))

            doc_pdf.build(story)
            return str(output_file)

        except ImportError:
            # 如果reportlab未安装，使用备用方法
            return ConversionService._word_to_pdf_fallback(input_path)

    @staticmethod
    def _word_to_pdf_fallback(input_path: str) -> str:
        """Word转PDF的备用方法（需要LibreOffice）"""
        import subprocess
        import platform

        input_file = Path(input_path)
        output_file = OUTPUT_DIR / f"{input_file.stem}.pdf"

        system = platform.system()

        if system == "Windows":
            # Windows: 使用LibreOffice
            libreoffice_paths = [
                r"C:\Program Files\LibreOffice\program\soffice.exe",
                r"C:\Program Files (x86)\LibreOffice\program\soffice.exe"
            ]
            soffice = None
            for path in libreoffice_paths:
                if Path(path).exists():
                    soffice = path
                    break

            if soffice:
                cmd = [
                    soffice,
                    "--headless",
                    "--convert-to", "pdf",
                    "--outdir", str(OUTPUT_DIR),
                    str(input_file)
                ]
                subprocess.run(cmd, check=True, capture_output=True)
                return str(output_file)

        elif system == "Linux":
            # Linux: 使用soffice
            subprocess.run(
                ["soffice", "--headless", "--convert-to", "pdf",
                 "--outdir", str(OUTPUT_DIR), str(input_file)],
                check=True, capture_output=True
            )
            return str(output_file)

        raise RuntimeError("需要安装LibreOffice才能转换.doc文件")

    @staticmethod
    def image_to_pdf(image_paths: list, output_name: Optional[str] = None) -> str:
        """多张图片转PDF"""
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.utils import ImageReader
        from reportlab.platypus import SimpleDocTemplate, Image as RLImage, Spacer
        from reportlab.lib.units import cm

        if not output_name:
            output_name = f"{uuid.uuid4().hex}.pdf"
        output_file = OUTPUT_DIR / output_name

        # 创建PDF
        doc = SimpleDocTemplate(
            str(output_file),
            pagesize=A4,
            rightMargin=1*cm,
            leftMargin=1*cm,
            topMargin=1*cm,
            bottomMargin=1*cm
        )

        story = []
        page_width, page_height = A4

        for img_path in image_paths:
            img = ImageReader(img_path)

            # 计算图片缩放比例以适应页面
            img_width = img.getWidth()
            img_height = img.getHeight()

            max_width = page_width - 2*cm
            max_height = page_height - 2*cm

            ratio = min(max_width/img_width, max_height/img_height)
            new_width = img_width * ratio
            new_height = img_height * ratio

            story.append(RLImage(img_path, width=new_width, height=new_height))
            story.append(Spacer(1, 0.5*cm))

        doc.build(story)
        return str(output_file)

    @staticmethod
    def pdf_merge(pdf_paths: list, output_name: Optional[str] = None) -> str:
        """合并多个PDF"""
        from PyPDF2 import PdfMerger

        if not output_name:
            output_name = f"{uuid.uuid4().hex}.pdf"
        output_file = OUTPUT_DIR / output_name

        merger = PdfMerger()
        for pdf_path in pdf_paths:
            merger.append(pdf_path)

        with open(output_file, 'wb') as f:
            merger.write(f)

        return str(output_file)


# 全局服务实例
conversion_service = ConversionService()
