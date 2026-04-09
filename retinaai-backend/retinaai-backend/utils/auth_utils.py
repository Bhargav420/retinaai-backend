from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
import os

# Secret key to sign JWT tokens
SECRET_KEY = "SUPER_SECRET_KEY_RETINAAI"  # Use env variable in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 1 week

# Bcrypt context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
MAX_BCRYPT_LENGTH = 72  # Bcrypt max password length in bytes

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies a plain password against a bcrypt hashed password.
    Truncates password to 72 characters to avoid bcrypt limitation.
    """
    if not hashed_password:
        return False
    try:
        truncated_pw = plain_password[:MAX_BCRYPT_LENGTH]
        return pwd_context.verify(truncated_pw, hashed_password)
    except ValueError:
        # This handles cases where the password_hash in the DB is not a valid hash
        # e.g., plain text passwords from manual entry, causing internal server error
        return plain_password == hashed_password

def get_password_hash(password: str) -> str:
    """
    Hashes a password using bcrypt.
    Truncates password to 72 characters to avoid bcrypt limitation.
    """
    truncated_pw = password[:MAX_BCRYPT_LENGTH]
    return pwd_context.hash(truncated_pw)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Creates a JWT access token with optional expiry.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt