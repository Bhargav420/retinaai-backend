from fastapi import APIRouter, Depends, HTTPException
from models.user import User
from routes.auth import get_current_user

router = APIRouter(prefix="/doctor", tags=["doctor"])


@router.get("/profile")
def get_doctor_profile(current_user: User = Depends(get_current_user)):

    if current_user.role != "Doctor":
        raise HTTPException(status_code=403, detail="Doctor only")

    return {
        "id": current_user.id,
        "full_name": current_user.full_name,
        "email": current_user.email,
        "phone": current_user.phone,
        "patient_code": current_user.patient_code,
        "medical_license_id": current_user.medical_license_id,
        "specialization": current_user.specialization,
        "hospital_name": current_user.hospital_name,
        "experience": current_user.experience,
        "created_at": current_user.created_at
    }