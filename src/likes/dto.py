from pydantic import BaseModel, Field


class LikeRequestDTO(BaseModel):
    user_id: int = Field(gt=0)
    property_id: int = Field(gt=0)

    class Config:
        extra = "forbid"


class DislikeRequestDTO(BaseModel):
    user_id: int = Field(gt=0)
    property_id: int = Field(gt=0)

    class Config:
        extra = "forbid"


class LikeResponseDTO(BaseModel):
    id: int
    user_id: int
    property_id: int

    class Config:
        extra = "forbid"
