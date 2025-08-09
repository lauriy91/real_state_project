from typing import Optional
from pydantic import BaseModel

class PropertyRequestDTO(BaseModel):
    address: str
    city: str
    price: float
    description: Optional[str] = None
    year: Optional[int] = None
    status: Optional[str] = None

    class Config:
        anystr_strip_whitespace = True
        extra = "forbid"

class PropertyUpdateDTO(BaseModel):
    address: Optional[str] = None
    city: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None
    year: Optional[int] = None
    status: Optional[str] = None

    class Config:
        anystr_strip_whitespace = True
        extra = "forbid"

class PropertyResponseDTO(BaseModel):
    id: int
    address: str
    city: str
    price: float
    description: Optional[str] = None
    year: Optional[int] = None
    status: Optional[str] = None

    class Config:
        anystr_strip_whitespace = True
        extra = "forbid"
