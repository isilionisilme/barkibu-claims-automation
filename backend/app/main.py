from fastapi import FastAPI
from .routes import router

app = FastAPI(title="Medical Records Processor")

@app.get("/health")
def health():
    return {"status":"Ok"}

app.include_router(router)