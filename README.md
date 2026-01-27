# Barkibu Claims Automation 
Technical exercise for automating ingestion and processing of veterinary medical records. 


## Backend setup (local)

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
