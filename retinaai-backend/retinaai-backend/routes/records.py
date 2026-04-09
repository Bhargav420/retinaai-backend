from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from database import get_session
from models.scan_record import ScanRecord
from typing import List
from fastapi.responses import StreamingResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
import os

from models.user import User

router = APIRouter(prefix="/records", tags=["records"])


# =========================
# PATIENT HISTORY
# =========================

@router.get("/patient/{patient_code}", response_model=List[ScanRecord])
def get_patient_history(
    patient_code: str,
    session: Session = Depends(get_session)
):

    records = session.exec(
        select(ScanRecord).where(ScanRecord.patient_code == patient_code)
    ).all()

    return records


# =========================
# DOCTOR DASHBOARD
# =========================

@router.get("/doctor/dashboard", response_model=List[ScanRecord])
def doctor_dashboard(session: Session = Depends(get_session)):

    records = session.exec(select(ScanRecord)).all()

    return records


# =========================
# DOWNLOAD REPORT (PDF)
# =========================

@router.get("/download/{scan_code}")
def download_scan_report(
    scan_code: str,
    session: Session = Depends(get_session)
):
    record = session.exec(
        select(ScanRecord).where(ScanRecord.scan_code == scan_code)
    ).first()

    if not record:
        return StreamingResponse(io.BytesIO(b"Record not found"), status_code=404)

    # Fetch patient name
    patient = session.exec(
        select(User).where(User.patient_code == record.patient_code)
    ).first()
    
    patient_name = patient.full_name if patient else "Unknown Patient"

    # Create PDF
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Header
    p.setFont("Helvetica-Bold", 24)
    p.drawCentredString(width/2, height - 1*inch, "RETINAAI DIAGNOSTIC REPORT")
    
    p.setStrokeColor(colors.cyan)
    p.line(1*inch, height - 1.2*inch, width - 1*inch, height - 1.2*inch)

    # Patient Details
    p.setFont("Helvetica-Bold", 14)
    p.drawString(1*inch, height - 1.6*inch, "PATIENT DETAILS")
    p.setFont("Helvetica", 12)
    p.drawString(1*inch, height - 1.9*inch, f"Name: {patient_name}")
    p.drawString(1*inch, height - 2.1*inch, f"ID: {record.patient_code}")
    p.drawString(1*inch, height - 2.3*inch, f"Date: {record.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")

    # Scan Details
    p.setFont("Helvetica-Bold", 14)
    p.drawString(1*inch, height - 2.8*inch, "DIAGNOSIS SUMMARY")
    p.setFont("Helvetica-Bold", 16)
    p.setFillColor(colors.red if "Retinopathy" in record.diagnosis else colors.green)
    p.drawString(1*inch, height - 3.1*inch, f"RESULT: {record.diagnosis}")
    
    p.setFillColor(colors.black)
    p.setFont("Helvetica", 12)
    p.drawString(1*inch, height - 3.4*inch, f"Severity Level: {record.severity}")
    p.drawString(1*inch, height - 3.6*inch, f"AI Confidence Score: {record.confidence * 100:.2f}%")
    p.drawString(1*inch, height - 3.8*inch, f"Scan Identifier: {record.scan_code}")

    # Image (if exists)
    if record.image_path and os.path.exists(record.image_path):
        try:
            p.drawImage(record.image_path, 1*inch, height - 7.5*inch, width=3*inch, height=3*inch, preserveAspectRatio=True)
            p.setFont("Helvetica-Oblique", 10)
            p.drawString(1*inch, height - 7.7*inch, "Captured Retinal Scan Image")
        except:
            p.drawString(1*inch, height - 4.5*inch, "[Image could not be embedded]")

    # Notes
    if record.notes:
        p.setFont("Helvetica-Bold", 12)
        p.drawString(1*inch, height - 8.2*inch, "Clinical Notes:")
        p.setFont("Helvetica", 10)
        p.drawString(1.2*inch, height - 8.4*inch, record.notes)

    # Disclaimer
    p.setStrokeColor(colors.lightgrey)
    p.line(1*inch, 1.5*inch, width - 1*inch, 1.5*inch)
    
    p.setFont("Helvetica-Bold", 10)
    p.setFillColor(colors.darkred)
    p.drawString(1*inch, 1.3*inch, "MEDICAL DISCLAIMER:")
    
    p.setFont("Helvetica", 8)
    p.setFillColor(colors.black)
    disclaimer_lines = [
        "1. RetinaAI is an AI-powered screening tool and is NOT 100% accurate.",
        "2. This report is for informational and prediction purposes only.",
        "3. The deep learning models are continuously evolving and learning.",
        "4. This result is NOT a final medical diagnosis. Always verify with a personal professional doctor.",
        "5. Do not assume this result solves the problem 100%. Clinical verification is mandatory."
    ]
    
    y_pos = 1.15*inch
    for line in disclaimer_lines:
        p.drawString(1*inch, y_pos, line)
        y_pos -= 0.15*inch

    # Footer
    p.setFont("Helvetica", 9)
    p.drawCentredString(width/2, 0.5*inch, "Generated securely by RetinaAi Healthcare Systems")

    p.showPage()
    p.save()

    buffer.seek(0)
    return StreamingResponse(
        buffer,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f"attachment; filename=RetinaAI_Report_{scan_code}.pdf"
        }
    )