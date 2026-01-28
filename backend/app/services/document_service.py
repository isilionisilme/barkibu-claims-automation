from uuid import UUID, uuid4
from datetime import datetime
from typing import Dict, Any
from ..db import get_connection, init_db


STATUS_UPLOADED = "UPLOADED"


def ensure_db():
    init_db()


def create_document(document_id: UUID, filename: str, content_type: str | None) -> Dict[str, Any]:
    ensure_db()
    conn = get_connection()
    cur = conn.cursor()
    now = datetime.utcnow().isoformat()
    cur.execute(
        "INSERT INTO documents(id, filename, content_type, created_at) VALUES (?, ?, ?, ?)",
        (str(document_id), filename, content_type, now),
    )
    cur.execute(
        "INSERT INTO document_status_history(document_id, status, changed_at) VALUES (?, ?, ?)",
        (str(document_id), STATUS_UPLOADED, now),
    )
    conn.commit()
    conn.close()
    return {
        "document_id": str(document_id),
        "filename": filename,
        "content_type": content_type,
        "status": STATUS_UPLOADED,
        "created_at": now,
    }


def get_document(document_id: UUID) -> Dict[str, Any] | None:
    ensure_db()
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, filename, content_type, created_at FROM documents WHERE id = ?", (str(document_id),))
    row = cur.fetchone()
    if not row:
        conn.close()
        return None
    cur.execute(
        "SELECT status, changed_at FROM document_status_history WHERE document_id = ? ORDER BY changed_at ASC",
        (str(document_id),),
    )
    history = [dict(status=r[0], changed_at=r[1]) for r in cur.fetchall()]
    conn.close()
    return {
        "document_id": row[0],
        "filename": row[1],
        "content_type": row[2],
        "created_at": row[3],
        "status_history": history,
    }
