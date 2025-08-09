from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class UserRequestDTO(BaseModel):
    nombre: str
    email: EmailStr
    password: str = Field(min_length=8)
    ciudad: Optional[str] = None
    telefono: Optional[str] = None

    class Config:
        anystr_strip_whitespace = True
        extra = "forbid"

class UserUpdateDTO(BaseModel):
    nombre: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(default=None, min_length=8)
    ciudad: Optional[str] = None
    telefono: Optional[str] = None

    class Config:
        anystr_strip_whitespace = True
        extra = "forbid"

class UserResponseDTO(BaseModel):
    id: int
    nombre: str
    email: EmailStr
    ciudad: Optional[str] = None
    telefono: Optional[str] = None

    class Config:
        anystr_strip_whitespace = True
        extra = "forbid"