from fastapi.testclient import TestClient
from app.main import app
from io import BytesIO


def test_upload_and_get_document():
    client = TestClient(app)
    file_content = b"hello world"
    files = {"file": ("sample.txt", BytesIO(file_content), "text/plain")}
    resp = client.post("/documents/upload", files=files)
    assert resp.status_code == 200
    body = resp.json()
    assert "document_id" in body
    doc_id = body["document_id"]

    get_resp = client.get(f"/documents/{doc_id}")
    assert get_resp.status_code == 200
    doc = get_resp.json()
    assert doc["document_id"] == doc_id
    assert doc["filename"] == "sample.txt"
    assert len(doc["status_history"]) >= 1
