from pydantic import BaseModel, EmailStr
from typing import Optional


# =========================================
# REGISTER
# =========================================

class RegisterRequest(BaseModel):

    full_name: str
    email: EmailStr
    phone: str
    password: str
    role: str

    medical_license_id: Optional[str] = None
    specialization: Optional[str] = None
    hospital_name: Optional[str] = None
    experience: Optional[str] = None


# =========================================
# LOGIN
# =========================================

class LoginRequest(BaseModel):

    email: Optional[EmailStr] = None
    medical_license_id: Optional[str] = None
    password: str


# =========================================
# VERIFY OTP (FOR REGISTRATION)
# =========================================

class VerifyOtpRequest(BaseModel):

    email: EmailStr
    otp: str


# =========================================
# FORGOT PASSWORD
# =========================================

class ForgotPasswordRequest(BaseModel):

    email: EmailStr


# =========================================
# VERIFY RESET OTP
# =========================================

class VerifyResetOtpRequest(BaseModel):

    email: EmailStr
    otp: str


# =========================================
# RESET PASSWORD
# =========================================

class ResetPasswordRequest(BaseModel):

    email: EmailStr
    new_password: str