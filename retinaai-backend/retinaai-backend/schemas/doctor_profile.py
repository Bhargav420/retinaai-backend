from pydantic import BaseModel
from typing import Optional

class DoctorProfileResponse(BaseModel):

    full_name: str
    email: str
    phone: str

    medical_license_id: Optional[str]
    specialization: Optional[str]
    hospital_name: Optional[str]
    experience: Optional[str]