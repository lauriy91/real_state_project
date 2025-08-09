from typing import Optional
from pydantic import BaseModel


class PropertyRequestDTO(BaseModel):
    status: str
    price: float
    address: str
    city: str
    description: str
    image_url: str
    property_type: str
    property_subtype: str
    property_size: float

    class Config:
        anystr_strip_whitespace = True
        extra = "forbid"


class PropertyUpdateDTO(BaseModel):
    status: Optional[str] = None
    price: Optional[float] = None
    address: Optional[str] = None
    city: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = None
    property_type: Optional[str] = None
    property_subtype: Optional[str] = None
    property_size: Optional[float] = None

    class Config:
        anystr_strip_whitespace = True
        extra = "forbid"


class PropertyResponseDTO(BaseModel):
    id: int
    status: str
    price: float
    address: str
    city: str
    description: str
    image_url: str
    property_type: str
    property_subtype: str
    property_size: float

    class Config:
        anystr_strip_whitespace = True
        extra = "forbid"
