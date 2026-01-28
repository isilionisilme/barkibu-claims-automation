from fastapi import APIRouter, UploadFile, File, HTTPException
from uuid import uuid4
from .schemas import UploadResponse, DocumentResponse
from .services.document_service import create_document, get_document

router = APIRouter()


@router.post("/documents/upload", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)) -> UploadResponse:
    # Generate id and persist minimal metadata + initial state
    doc_id = uuid4()
    result = create_document(doc_id, file.filename, file.content_type)
    return UploadResponse(
        document_id=result["document_id"],
        filename=result["filename"],
        content_type=result["content_type"],
        status=result["status"],
    )


@router.get("/documents/{document_id}", response_model=DocumentResponse)
def get_document_endpoint(document_id: str):
    record = get_document(document_id)
    if not record:
        raise HTTPException(status_code=404, detail="document not found")
    return DocumentResponse(**record)