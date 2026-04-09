from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class User(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)

    patient_code: Optional[str] = None
    full_name: str
    email: str
    phone: str

    password_hash: Optional[str] = None
    role: str

    is_verified: bool = Field(default=False)
    is_active: bool = Field(default=True)

    otp_code: Optional[str] = None
    otp_expiry: Optional[datetime] = None

    medical_license_id: Optional[str] = None
    specialization: Optional[str] = None
    hospital_name: Optional[str] = None
    experience: Optional[str] = None

    created_at: datetime = Field(default_factory=datetime.utcnow)