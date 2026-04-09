from pydantic import BaseModel

class SetPasswordRequest(BaseModel):
    email: str
    password: str