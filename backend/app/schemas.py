from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class UploadResponse(BaseModel):
    document_id: UUID
    filename: str
    content_type: str | None
    status: str # "uploaded"
