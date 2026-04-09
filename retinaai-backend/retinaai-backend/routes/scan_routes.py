from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
import shutil
import uuid
import os
from sqlmodel import Session, select
from database import get_session
from models.scan_record import ScanRecord
from models.user import User
from services.ai_service import predict_retina

router = APIRouter(prefix="/scan", tags=["scan"])

UPLOAD_FOLDER = "uploads/"


@router.post("/")
async def scan_retina(
    patient_code: str,
    file: UploadFile = File(...),
    session: Session = Depends(get_session)
):

    # ----------------------------
    # Verify patient exists
    # ----------------------------

    patient = session.exec(
        select(User).where(User.patient_code == patient_code)
    ).first()

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    # ----------------------------
    # Ensure upload folder exists
    # ----------------------------

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    # ----------------------------
    # Save uploaded image
    # ----------------------------

    filename = str(uuid.uuid4()) + ".jpg"
    path = os.path.join(UPLOAD_FOLDER, filename)

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # ----------------------------
    # Run AI prediction
    # ----------------------------

    result = predict_retina(path)

    # ----------------------------
    # Save scan record
    # ----------------------------

    scan = ScanRecord(
        patient_code=patient_code,
        image_path=path,
        diagnosis=result["diagnosis"],
        severity=result["diagnosis"],
        confidence=result["confidence"]
    )

    session.add(scan)
    session.commit()
    session.refresh(scan)

    # ----------------------------
    # Generate Scan Code
    # ----------------------------

    scan.scan_code = f"RA-SCAN-{scan.id:04d}"

    session.add(scan)
    session.commit()
    session.refresh(scan)

    # ----------------------------
    # Return response
    # ----------------------------

    return {
        "scan_code": scan.scan_code,
        "patient_code": patient_code,
        "diagnosis": result["diagnosis"],
        "confidence": result["confidence"],
        "probabilities": result["probabilities"]
    }