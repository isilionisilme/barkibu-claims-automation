from fastapi import APIRouter, UploadFile, File
from uuid import uuid4
from .schemas import UploadResponse

router = APIRouter()
@router.post("/documents/upload", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)) -> UploadResponse:
    doc_id = uuid4()

    return UploadResponse(
        document_id=doc_id,
        filename=file.filename,
        content_type=file.content_type,
        status="Uploaded"
    )