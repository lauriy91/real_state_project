from typing import Dict, List, Optional

from src.users.dto import UserRequestDTO, UserUpdateDTO, UserResponseDTO
from src.users import repository

def list_users(limit: int = 200, offset: int = 0) -> List[UserResponseDTO]:
    rows = repository.find_all(limit=limit, offset=offset)
    return [
        UserResponseDTO(
            id=r["id"],
            name=r["name"],
            email=r["email"],
            city=r.get("city"),
            phone=r.get("phone"),
        )
        for r in rows
    ]

def get_user(user_id: int) -> Optional[UserResponseDTO]:
    row = repository.find_by_id(user_id)
    if not row:
        return None
    return UserResponseDTO(
        id=row["id"],
        name=row["name"],
        email=row["email"],
        city=row.get("city"),
        phone=row.get("phone"),
    )

def create_user(dto: UserRequestDTO) -> UserResponseDTO:
    if repository.exists_email(dto.email):
        raise ValueError("Email ya registrado")
    new_id = repository.insert_user(
        {
            "name": dto.name,
            "email": dto.email,
            "password": dto.password,
            "city": dto.city,
            "phone": dto.phone,
            "active": True,
        }
    )
    return UserResponseDTO(
        id=new_id,
        name=dto.name,
        email=dto.email,
        city=dto.city,
        phone=dto.phone,
    )

def update_user(user_id: int, dto: UserUpdateDTO) -> Optional[UserResponseDTO]:
    data: Dict = {}
    if dto.name is not None:
        data["name"] = dto.name
    if dto.password is not None:
        data["password"] = dto.password
    if dto.city is not None:
        data["city"] = dto.city
    if dto.phone is not None:
        data["phone"] = dto.phone

    updated = repository.update_user(user_id, data)
    if updated <= 0:
        return None
    return get_user(user_id)

def delete_user(user_id: int) -> bool:
    deleted = repository.delete_user(user_id)
    return deleted > 0
