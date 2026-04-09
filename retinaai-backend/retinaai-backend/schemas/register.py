from pydantic import BaseModel

class RegisterRequest(BaseModel):
    full_name: str
    email: str
    phone: str
    role: str