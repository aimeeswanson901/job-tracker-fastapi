from sqlmodel import SQLModel
from typing import Optional


class JobCreate(SQLModel):
    role: str
    company: str
    status: Optional[str] = "Applied"
    link: Optional[str] = None
    notes: Optional[str] = None


class JobUpdate(SQLModel):
    role: Optional[str] = None
    company: Optional[str] = None
    status: Optional[str] = None
    link: Optional[str] = None
    notes: Optional[str] = None
