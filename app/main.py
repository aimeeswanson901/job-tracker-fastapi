from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from sqlmodel import Session, select
from app.db import get_session, init_db
from app.models import JobApplication
from app.schemas import JobCreate, JobUpdate

app = FastAPI(title="Job Tracker API")

app.mount("/", StaticFiles(directory="static", html=True), name="static")


@app.on_event("startup")
def on_startup():
    init_db()


@app.post("/applications", response_model=JobApplication)
def create_job(job: JobCreate, session: Session = Depends(get_session)):
    db_job = JobApplication(**job.dict())
    session.add(db_job)
    session.commit()
    session.refresh(db_job)
    return db_job


@app.get("/applications")
def list_jobs(status: str = None, company: str = None, session: Session = Depends(get_session)):
    query = select(JobApplication)
    if status:
        query = query.where(JobApplication.status == status)
    if company:
        query = query.where(JobApplication.company.contains(company))
    return session.exec(query).all()


@app.get("/applications/{job_id}", response_model=JobApplication)
def get_job(job_id: int, session: Session = Depends(get_session)):
    job = session.get(JobApplication, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Not found")
    return job


@app.patch("/applications/{job_id}", response_model=JobApplication)
def update_job(job_id: int, job: JobUpdate, session: Session = Depends(get_session)):
    db_job = session.get(JobApplication, job_id)
    if not db_job:
        raise HTTPException(status_code=404, detail="Not found")
    data = job.dict(exclude_unset=True)
    for k, v in data.items():
        setattr(db_job, k, v)
    session.add(db_job)
    session.commit()
    session.refresh(db_job)
    return db_job


@app.delete("/applications/{job_id}")
def delete_job(job_id: int, session: Session = Depends(get_session)):
    db_job = session.get(JobApplication, job_id)
    if not db_job:
        raise HTTPException(status_code=404, detail="Not found")
    session.delete(db_job)
    session.commit()
    return {"ok": True}
