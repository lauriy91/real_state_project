from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserRequestDTO(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(min_length=8)
    city: Optional[str] = None
    phone: Optional[str] = None

    class Config:
        anystr_strip_whitespace = True
        extra = "forbid"


class UserUpdateDTO(BaseModel):
    name: Optional[str] = None
    password: Optional[str] = Field(default=None, min_length=8)
    city: Optional[str] = None
    phone: Optional[str] = None

    class Config:
        anystr_strip_whitespace = True
        extra = "forbid"


class UserResponseDTO(BaseModel):
    id: int
    name: str
    email: EmailStr
    city: Optional[str] = None
    phone: Optional[str] = None

    class Config:
        anystr_strip_whitespace = True
        extra = "forbid"
