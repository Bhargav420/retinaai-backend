from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session, select, SQLModel
from jose import jwt, JWTError
from datetime import datetime, timedelta

from database import get_session
from models.user import User

from schemas.auth_schema import (
    RegisterRequest,
    LoginRequest,
    VerifyOtpRequest,
    ForgotPasswordRequest,
    VerifyResetOtpRequest,
    ResetPasswordRequest
)

from utils.auth_utils import (
    get_password_hash,
    verify_password,
    create_access_token,
    SECRET_KEY,
    ALGORITHM
)

from utils.otp_utils import generate_otp
from utils.email_utils import send_otp_email

router = APIRouter(prefix="/auth", tags=["auth"])


# =========================
# REGISTER → SEND OTP
# =========================

@router.post("/register")
async def register(user_data: RegisterRequest, session: Session = Depends(get_session)):

    existing_user = session.exec(
        select(User).where(User.email == user_data.email).where(User.is_active == True)
    ).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered and active")

    if user_data.role == "Doctor" and user_data.medical_license_id:
        existing_doc = session.exec(
            select(User).where(User.medical_license_id == user_data.medical_license_id)
        ).first()

        if existing_doc:
            raise HTTPException(
                status_code=400,
                detail="Medical License ID already registered"
            )

    otp = generate_otp()

    new_user = User(
        full_name=user_data.full_name,
        email=user_data.email,
        phone=user_data.phone,
        password_hash=get_password_hash(user_data.password),
        role=user_data.role,
        medical_license_id=user_data.medical_license_id,
        specialization=user_data.specialization,
        hospital_name=user_data.hospital_name,
        experience=user_data.experience,
        otp_code=otp,
        otp_expiry=datetime.utcnow() + timedelta(minutes=5),
        is_verified=False
    )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    if new_user.role.lower() == "patient":
        new_user.patient_code = f"RA-PAT-{new_user.id:04d}"
    else:
        new_user.patient_code = f"RA-DOC-{new_user.id:04d}"

    session.add(new_user)
    session.commit()

    # SEND VERIFICATION EMAIL
    try:
        send_otp_email(user_data.email, otp, user_data.role, "verify")
    except Exception as e:
        print(f"Email error: {e}")

    return {
        "message": "OTP sent to email",
        "patient_code": new_user.patient_code
    }


# =========================
# VERIFY OTP
# =========================

@router.post("/verify-otp")
async def verify_otp(data: VerifyOtpRequest, session: Session = Depends(get_session)):

    user = session.exec(
        select(User).where(User.email == data.email)
    ).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.otp_code != data.otp:
        raise HTTPException(status_code=400, detail="Invalid OTP")

    if datetime.utcnow() > user.otp_expiry:
        raise HTTPException(status_code=400, detail="OTP expired")

    user.is_verified = True
    user.otp_code = None
    user.otp_expiry = None

    session.add(user)
    session.commit()

    access_token = create_access_token(
        data={"sub": user.email, "role": user.role}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# =========================
# LOGIN
# =========================

@router.post("/login")
async def login(login_data: LoginRequest, session: Session = Depends(get_session)):
    
    user = None
    if login_data.email:
        email = login_data.email.strip()
        user = session.exec(
            select(User).where(User.email == email)
        ).first()

    elif login_data.medical_license_id:
        ml_id = login_data.medical_license_id.strip()
        # Doctors can login using either their License ID or their Email
        user = session.exec(
            select(User).where(
                (User.medical_license_id == ml_id) | (User.email == ml_id)
            )
        ).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not user.is_verified:
        raise HTTPException(
            status_code=403,
            detail={"message": "Email not verified", "email": user.email}
        )

    if not verify_password(login_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect credentials"
        )

    access_token = create_access_token(
        data={"sub": user.email, "role": user.role}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# =========================
# FORGOT PASSWORD → SEND OTP
# =========================

@router.post("/forgot-password")
async def forgot_password(data: ForgotPasswordRequest, session: Session = Depends(get_session)):

    user = session.exec(
        select(User).where(User.email == data.email)
    ).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    otp = generate_otp()

    user.otp_code = otp
    user.otp_expiry = datetime.utcnow() + timedelta(minutes=5)

    session.add(user)
    session.commit()

    # SEND RESET PASSWORD EMAIL
    send_otp_email(user.email, otp, user.role, "reset")

    return {"message": "Reset OTP sent to email"}


# =========================
# VERIFY RESET OTP
# =========================

@router.post("/verify-reset-otp")
async def verify_reset_otp(data: VerifyResetOtpRequest, session: Session = Depends(get_session)):

    user = session.exec(
        select(User).where(User.email == data.email)
    ).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.otp_code != data.otp:
        raise HTTPException(status_code=400, detail="Invalid OTP")

    if datetime.utcnow() > user.otp_expiry:
        raise HTTPException(status_code=400, detail="OTP expired")

    return {"message": "OTP verified"}


# =========================
# RESET PASSWORD
# =========================

@router.post("/reset-password")
async def reset_password(data: ResetPasswordRequest, session: Session = Depends(get_session)):

    user = session.exec(
        select(User).where(User.email == data.email)
    ).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.password_hash = get_password_hash(data.new_password)

    user.otp_code = None
    user.otp_expiry = None

    session.add(user)
    session.commit()

    return {"message": "Password reset successful"}


# =========================
# TOKEN AUTH
# =========================

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    session: Session = Depends(get_session)
):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")

        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = session.exec(
        select(User).where(User.email == email)
    ).first()

    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return user


# =========================
# GET PROFILE
# =========================

@router.get("/me")
async def get_profile(current_user: User = Depends(get_current_user)):

    return {
        "id": current_user.id,
        "patient_code": current_user.patient_code or "",
        "full_name": current_user.full_name or "User",
        "email": current_user.email,
        "phone": current_user.phone or "",
        "role": current_user.role
    }
# =========================
# UPDATE PROFILE
# =========================

class UpdateProfileRequest(SQLModel):
    phone: str

@router.put("/profile")
async def update_profile(
    data: UpdateProfileRequest,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    current_user.phone = data.phone
    session.add(current_user)
    session.commit()
    return {"message": "Profile updated successfully"}


# =========================
# DEACTIVATE ACCOUNT
# =========================

@router.post("/deactivate")
async def deactivate_account(
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    # Rename email to allow reuse while preserving history
    original_email = current_user.email
    current_user.email = f"deactivated_{current_user.id}_{original_email}"
    current_user.is_active = False
    
    session.add(current_user)
    session.commit()
    
    return {"message": "Account deactivated successfully"}
