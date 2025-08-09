from typing import Dict, List, Optional

from src.likes.dto import LikeRequestDTO, DislikeRequestDTO, LikeResponseDTO
from src.likes import repository


def create_like(dto: LikeRequestDTO) -> LikeResponseDTO:
    existing_id = repository.exists_id(dto.user_id, dto.property_id)
    if existing_id:
        repository.delete_like(existing_id if isinstance(existing_id, int) else existing_id[0])
        return LikeResponseDTO(id=0, user_id=dto.user_id, property_id=dto.property_id)

    new_id = repository.insert_like(
        {
            "user_id": dto.user_id,
            "property_id": dto.property_id,
        }
    )
    return LikeResponseDTO(
        id=new_id,
        user_id=dto.user_id,
        property_id=dto.property_id,
    )

def create_dislike(dto: DislikeRequestDTO) -> LikeResponseDTO:
    if repository.exists_id(dto.user_id, dto.property_id):
        raise ValueError("ID ya registrado")
    new_id = repository.insert_dislike(
        {
            "user_id": dto.user_id,
            "property_id": dto.property_id,
        }
    )
    return LikeResponseDTO(
        id=new_id,
        user_id=dto.user_id,
        property_id=dto.property_id,
    )


def delete_like(like_id: int) -> bool:
    deleted = repository.delete_like(like_id)
    return deleted > 0
