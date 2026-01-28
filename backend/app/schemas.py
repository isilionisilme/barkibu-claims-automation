from pydantic import BaseModel
from typing import Optional, List


class UploadResponse(BaseModel):
    document_id: str
    filename: str
    content_type: Optional[str]
    status: str


class StatusHistoryItem(BaseModel):
    status: str
    changed_at: str


class DocumentResponse(BaseModel):
    document_id: str
    filename: str
    content_type: Optional[str]
    created_at: str
    status_history: List[StatusHistoryItem]
