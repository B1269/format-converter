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
        根据文件类型选择转换策略：
        - .docx: 使用python-docx + reportlab
        - .doc: 使用LibreOffice（更可靠）
        """
        import logging
        logger = logging.getLogger(__name__)

        input_file = Path(input_path)
        ext = input_file.suffix.lower()

        logger.info(f"开始Word转PDF，文件: {input_file.name}, 扩展名: {ext}")

        # .doc 文件直接用LibreOffice转换（python-docx不支持.doc）
        if ext == '.doc':
            logger.info("检测到.doc文件，使用LibreOffice转换")
            return ConversionService._word_to_pdf_fallback(input_path)

        # .docx 文件使用python-docx + reportlab
        if ext == '.docx':
            logger.info("检测到.docx文件，使用python-docx + reportlab转换")
            try:
                from docx import Document
                from reportlab.lib.pagesizes import A4
                from reportlab.lib.styles import getSampleStyleSheet
                from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
                from reportlab.lib.units import cm

                # 读取Word文档
                doc = Document(input_path)

                output_file = OUTPUT_DIR / f"{input_file.stem}.pdf"

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
                logger.info(f"转换成功: {output_file}")
                return str(output_file)

            except ImportError as e:
                logger.warning(f"reportlab未安装: {e}，尝试使用LibreOffice")
                return ConversionService._word_to_pdf_fallback(input_path)
            except Exception as e:
                logger.error(f"python-docx转换失败: {e}，尝试使用LibreOffice")
                return ConversionService._word_to_pdf_fallback(input_path)

        raise ValueError(f"不支持的文件格式: {ext}，仅支持.doc和.docx")

    @staticmethod
    def _word_to_pdf_fallback(input_path: str) -> str:
        """Word转PDF的备用方法（需要LibreOffice）"""
        import subprocess
        import platform
        import logging
        import shutil

        logger = logging.getLogger(__name__)

        input_file = Path(input_path)
        output_file = OUTPUT_DIR / f"{input_file.stem}.pdf"

        system = platform.system()
        logger.info(f"LibreOffice转换: {input_file.name}, 系统: {system}")

        soffice = None

        if system == "Windows":
            # Windows: 搜索LibreOffice
            libreoffice_paths = [
                r"C:\Program Files\LibreOffice\program\soffice.exe",
                r"C:\Program Files (x86)\LibreOffice\program\soffice.exe",
                r"D:\LibreOffice\program\soffice.exe",
            ]
            for path in libreoffice_paths:
                if Path(path).exists():
                    soffice = path
                    break

            # 如果找不到，尝试从环境变量PATH中查找
            if not soffice:
                soffice_cmd = shutil.which("soffice")
                if soffice_cmd:
                    soffice = soffice_cmd

        elif system == "Linux":
            soffice = shutil.which("soffice")

        if not soffice:
            logger.error("未找到LibreOffice，请安装LibreOffice")
            raise RuntimeError(
                "需要安装LibreOffice才能转换此文件。\n"
                "Windows下载: https://www.libreoffice.org/download/download/\n"
                "安装后重启后端服务即可。"
            )

        logger.info(f"使用LibreOffice: {soffice}")

        try:
            cmd = [
                soffice,
                "--headless",
                "--convert-to", "pdf",
                "--outdir", str(OUTPUT_DIR),
                str(input_file)
            ]
            result = subprocess.run(
                cmd,
                check=True,
                capture_output=True,
                text=True,
                timeout=120  # 2分钟超时
            )
            logger.info(f"LibreOffice转换成功: {output_file}")
            return str(output_file)

        except subprocess.TimeoutExpired:
            logger.error("LibreOffice转换超时（超过2分钟）")
            raise RuntimeError("转换超时，文件可能过大或格式复杂")
        except subprocess.CalledProcessError as e:
            logger.error(f"LibreOffice转换失败: {e.stderr}")
            raise RuntimeError(f"LibreOffice转换失败: {e.stderr or '未知错误'}")
        except Exception as e:
            logger.error(f"LibreOffice转换异常: {e}")
            raise RuntimeError(f"转换失败: {str(e)}")

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

    @staticmethod
    def parse_document_text(input_path: str) -> dict:
        """
        解析文档文本内容
        支持 .docx, .doc, .pdf 三种格式
        返回：{ title: str, sections: list, full_text: str }
        """
        import logging
        logger = logging.getLogger(__name__)

        input_file = Path(input_path)
        ext = input_file.suffix.lower()
        logger.info(f"解析文档内容，文件: {input_file.name}, 扩展名: {ext}")

        if ext == '.docx':
            return ConversionService._parse_docx(input_path)
        elif ext == '.doc':
            return ConversionService._parse_doc(input_path)
        elif ext == '.pdf':
            return ConversionService._parse_pdf(input_path)
        else:
            raise ValueError(f"不支持的文件格式: {ext}，仅支持.docx、.doc、.pdf")

    @staticmethod
    def _parse_docx(input_path: str) -> dict:
        """解析 .docx 文件"""
        from docx import Document

        doc = Document(input_path)
        sections = []
        current_section = {"title": "正文", "paragraphs": []}

        for para in doc.paragraphs:
            text = para.text.strip()
            if not text:
                continue

            # 根据样式判断是否为标题
            style_name = para.style.name if para.style else ""
            if style_name.startswith('Heading') or '标题' in style_name:
                # 保存当前section，开始新section
                if current_section["paragraphs"]:
                    sections.append(current_section)
                current_section = {"title": text, "paragraphs": []}
            else:
                current_section["paragraphs"].append(text)

        # 保存最后一个section
        if current_section["paragraphs"]:
            sections.append(current_section)

        # 如果没有内容，创建一个默认section
        if not sections:
            sections.append({"title": "正文", "paragraphs": []})

        # 提取文档标题（第一个标题或文件名）
        title = sections[0]["title"] if sections else Path(input_path).stem

        return {
            "title": title,
            "sections": sections,
            "file_type": "docx"
        }

    @staticmethod
    def _parse_doc(input_path: str) -> dict:
        """解析 .doc 文件（使用LibreOffice转换为临时docx再解析）"""
        import subprocess
        import shutil
        import platform
        import tempfile

        logger = logging.getLogger(__name__)

        # 创建临时目录
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            input_file = Path(input_path)

            # 使用LibreOffice转换为docx
            soffice = None
            system = platform.system()

            if system == "Windows":
                libreoffice_paths = [
                    r"C:\Program Files\LibreOffice\program\soffice.exe",
                    r"C:\Program Files (x86)\LibreOffice\program\soffice.exe",
                ]
                for path in libreoffice_paths:
                    if Path(path).exists():
                        soffice = path
                        break
                if not soffice:
                    soffice = shutil.which("soffice")
            elif system == "Linux":
                soffice = shutil.which("soffice")

            if not soffice:
                logger.warning("LibreOffice未安装，尝试直接读取.doc文件")
                # 尝试直接读取（可能失败）
                try:
                    from docx import Document
                    doc = Document(input_path)
                    paragraphs = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
                    return {
                        "title": Path(input_path).stem,
                        "sections": [{"title": "正文", "paragraphs": paragraphs}],
                        "file_type": "doc"
                    }
                except:
                    raise RuntimeError("无法解析.doc文件，请安装LibreOffice")

            # 执行转换
            cmd = [
                soffice,
                "--headless",
                "--convert-to", "docx",
                "--outdir", str(temp_path),
                str(input_file)
            ]

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            if result.returncode != 0:
                raise RuntimeError(f"LibreOffice转换失败: {result.stderr}")

            # 找到转换后的docx文件
            docx_files = list(temp_path.glob("*.docx"))
            if not docx_files:
                raise RuntimeError("LibreOffice转换未生成docx文件")

            # 解析docx
            return ConversionService._parse_docx(str(docx_files[0]))

    @staticmethod
    def _parse_pdf(input_path: str) -> dict:
        """解析 .pdf 文件"""
        from PyPDF2 import PdfReader

        reader = PdfReader(input_path)
        sections = []
        current_section = {"title": "正文", "paragraphs": []}

        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if not text:
                continue

            # 按行分割，清理空白
            lines = [line.strip() for line in text.split('\n') if line.strip()]

            for line in lines:
                # 检测是否为页码或短行（可能是标题）
                if len(line) < 50 and i == 0:
                    # 可能是标题
                    if current_section["paragraphs"]:
                        sections.append(current_section)
                    current_section = {"title": line, "paragraphs": []}
                else:
                    current_section["paragraphs"].append(line)

        # 保存最后一个section
        if current_section["paragraphs"]:
            sections.append(current_section)

        # 如果没有内容，创建一个默认section
        if not sections:
            sections.append({"title": "正文", "paragraphs": []})

        title = sections[0]["title"] if sections else Path(input_path).stem

        return {
            "title": title,
            "sections": sections,
            "file_type": "pdf"
        }

    @staticmethod
    def pdf_to_word(input_path: str) -> str:
        """
        PDF转Word
        简化实现：提取PDF文本并创建Word文档
        复杂PDF（如扫描件、图文混排）需要使用pdf2docx等专门库
        """
        from docx import Document
        from PyPDF2 import PdfReader

        input_file = Path(input_path)
        output_file = OUTPUT_DIR / f"{input_file.stem}.docx"

        # 读取PDF
        reader = PdfReader(input_path)

        # 创建Word文档
        doc = Document()
        doc.add_heading(input_file.stem, 0)

        # 提取每页文本
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text.strip():
                # 添加页面标题
                doc.add_heading(f'第 {i+1} 页', level=2)
                # 添加文本内容
                doc.add_paragraph(text)

        # 保存
        doc.save(str(output_file))
        return str(output_file)


# 全局服务实例
conversion_service = ConversionService()
