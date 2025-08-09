from pydantic import BaseModel, EmailStr, Field


class LoginRequestDTO(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)

    class Config:
        anystr_strip_whitespace = True
        extra = "forbid"


class LoginResponseDTO(BaseModel):
    access_token: str
    token_type: str = "bearer"

    class Config:
        anystr_strip_whitespace = True
        extra = "forbid"


