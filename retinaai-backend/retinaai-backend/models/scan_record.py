from sqlmodel import SQLModel, Field
from typing import Optional
import datetime


class ScanRecord(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)

    patient_code: str
    scan_code: Optional[str] = None

    image_path: str

    diagnosis: str
    severity: str
    confidence: float

    timestamp: datetime.datetime = Field(
        default_factory=datetime.datetime.utcnow
    )

    notes: Optional[str] = None