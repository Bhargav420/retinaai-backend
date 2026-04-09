# routes/chat.py

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_session
from models.scan_record import ScanRecord
from models.user import User
from dotenv import load_dotenv
load_dotenv()
import requests
import os

router = APIRouter(prefix="/chat", tags=["chat"])


# =========================
# GROQ CONFIG
# =========================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

print("Loaded GROQ KEY:", GROQ_API_KEY)

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}


# =========================
# MEDICAL CHAT ASSISTANT
# =========================

@router.post("/assistant")
def medical_chat(
    patient_code: str,
    question: str,
    session: Session = Depends(get_session)
):

    try:

        # -------------------------
        # Fetch patient
        # -------------------------

        patient = session.exec(
            select(User).where(User.patient_code == patient_code)
        ).first()

        if not patient:
            raise HTTPException(
                status_code=404,
                detail="Patient not found"
            )

        # If user asks for name, respond directly (safer than AI)
        if "name" in question.lower():
            return {
                "patient_code": patient_code,
                "reply": f"Your registered name is {patient.full_name}."
            }

        # -------------------------
        # Fetch scan records
        # -------------------------

        scans = session.exec(
            select(ScanRecord).where(
                ScanRecord.patient_code == patient_code
            )
        ).all()

        if not scans:
            raise HTTPException(
                status_code=404,
                detail="No scan records found"
            )

        # -------------------------
        # Latest scan
        # -------------------------

        latest_scan = scans[-1]

        latest_summary = f"""
Latest Scan Result:
Scan Code: {latest_scan.scan_code}
Diagnosis: {latest_scan.diagnosis}
Severity: {latest_scan.severity}
Confidence: {round(latest_scan.confidence * 100, 2)}%
Date: {latest_scan.timestamp}
"""

        # -------------------------
        # Full scan history
        # -------------------------

        history = ""

        for s in scans:
            history += f"""
Scan Code: {s.scan_code}
Diagnosis: {s.diagnosis}
Severity: {s.severity}
Confidence: {round(s.confidence * 100, 2)}%
Date: {s.timestamp}
"""

        # -------------------------
        # AI Prompt
        # -------------------------

        prompt = f"""
You are RetinaAI Medical Assistant.

Patient Code: {patient_code}

{latest_summary}

Full Scan History:
{history}

Rules:
- Only answer questions related to diabetic retinopathy.
- Never reveal private information such as email, phone, or password.
- Only use the scan data provided.
- If the question is unrelated say:
"I can only provide medical insights related to retinal scans."

Patient Question:
{question}
"""

        # -------------------------
        # GROQ payload
        # -------------------------

        payload = {
            "model": "llama-3.1-8b-instant",
            "messages": [
                {
                    "role": "system",
                    "content": "You are RetinaAI medical assistant specialized in diabetic retinopathy."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.3,
            "max_tokens": 200
        }

        # -------------------------
        # Call Groq API
        # -------------------------

        response = requests.post(
            GROQ_URL,
            headers=headers,
            json=payload
        )

        print("GROQ STATUS:", response.status_code)
        print("GROQ RESPONSE:", response.text)

        if response.status_code != 200:
            raise HTTPException(
                status_code=500,
                detail=response.text
            )

        data = response.json()

        reply = data["choices"][0]["message"]["content"]

        return {
            "patient_code": patient_code,
            "reply": reply
        }

    except HTTPException:
        raise
    except HTTPException:
        raise
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )