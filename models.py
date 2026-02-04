from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class JobApplication(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    role: str
    company: str
    status: str = "Applied"
    link: Optional[str] = None
    notes: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
