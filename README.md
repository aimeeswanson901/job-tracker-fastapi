# Job Tracker (FastAPI + PostgreSQL + Simple UI)

A small, portfolio‑friendly job tracker app using FastAPI, SQLModel, and PostgreSQL.

## Features
- Create, read, update, delete job applications
- Filter by status and company
- Simple HTML UI (no frontend framework)

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# edit DATABASE_URL in .env
uvicorn app.main:app --reload
```

Open: http://127.0.0.1:8000

## API Endpoints
- POST /applications
- GET /applications
- GET /applications/{id}
- PATCH /applications/{id}
- DELETE /applications/{id}

## Notes
- Uses SQLModel for ORM
- Static UI served from /static
