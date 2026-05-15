"""
文件转换API
"""
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from typing import List
import os

from app.services.converter import conversion_service
from app.core.config import MAX_FILE_SIZE, SUPPORTED_CONVERSIONS

router = APIRouter()


@router.post("/convert/word-to-pdf")
async def convert_word_to_pdf(file: UploadFile = File(...)):
    """Word转PDF"""
    import logging
    logger = logging.getLogger(__name__)

    # 验证文件类型
    if not file.filename.lower().endswith(('.docx', '.doc')):
        raise HTTPException(status_code=400, detail="仅支持.docx或.doc文件")

    try:
        logger.info(f"收到Word转PDF请求: {file.filename}")

        # 保存上传文件
        input_path = await conversion_service.save_upload_file(file)
        logger.info(f"文件已保存: {input_path}")

        # 转换
        output_path = conversion_service.word_to_pdf(input_path)
        logger.info(f"转换成功: {output_path}")

        # 返回文件
        return FileResponse(
            path=output_path,
            filename=os.path.basename(output_path),
            media_type='application/pdf'
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Word转PDF失败: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/convert/image-to-pdf")
async def convert_image_to_pdf(files: List[UploadFile] = File(...)):
    """多张图片转PDF"""
    if len(files) < 1:
        raise HTTPException(status_code=400, detail="请至少上传一张图片")

    try:
        # 保存上传文件
        image_paths = []
        for file in files:
            if not file.filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
                raise HTTPException(status_code=400, detail=f"不支持的文件类型: {file.filename}")
            path = await conversion_service.save_upload_file(file)
            image_paths.append(path)

        # 转换
        output_path = conversion_service.image_to_pdf(image_paths)

        return FileResponse(
            path=output_path,
            filename=os.path.basename(output_path),
            media_type='application/pdf'
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/convert/pdf-merge")
async def merge_pdf(files: List[UploadFile] = File(...)):
    """合并PDF"""
    if len(files) < 2:
        raise HTTPException(status_code=400, detail="请至少上传两个PDF文件")

    try:
        # 保存上传文件
        pdf_paths = []
        for file in files:
            if not file.filename.lower().endswith('.pdf'):
                raise HTTPException(status_code=400, detail=f"仅支持PDF文件: {file.filename}")
            path = await conversion_service.save_upload_file(file)
            pdf_paths.append(path)

        # 合并
        output_path = conversion_service.pdf_merge(pdf_paths)

        return FileResponse(
            path=output_path,
            filename=os.path.basename(output_path),
            media_type='application/pdf'
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/convert/pdf-to-word")
async def convert_pdf_to_word(file: UploadFile = File(...)):
    """PDF转Word"""
    import logging
    logger = logging.getLogger(__name__)

    # 验证文件类型
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="仅支持PDF文件")

    try:
        logger.info(f"收到PDF转Word请求: {file.filename}")

        # 保存上传文件
        input_path = await conversion_service.save_upload_file(file)
        logger.info(f"文件已保存: {input_path}")

        # 转换
        output_path = conversion_service.pdf_to_word(input_path)
        logger.info(f"转换成功: {output_path}")

        # 返回文件
        return FileResponse(
            path=output_path,
            filename=os.path.basename(output_path),
            media_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"PDF转Word失败: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/supported-conversions")
async def get_supported_conversions():
    """获取支持的转换类型"""
    return SUPPORTED_CONVERSIONS
