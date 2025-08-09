from typing import Dict, List, Optional

from src.properties.dto import (
    PropertyRequestDTO,
    PropertyUpdateDTO,
    PropertyResponseDTO,
)
from src.properties import repository

def list_properties(limit: int = 20, offset: int = 0, filters: Optional[Dict] = None) -> List[PropertyResponseDTO]:
    rows = repository.find_all(limit=limit, offset=offset, filters=filters)
    return [
        PropertyResponseDTO(
            id=r["id"],
            address=r["address"],
            city=r["city"],
            price=r["price"],
            description=r.get("description"),
            year=r.get("year"),
            status=r.get("status"),
        )
        for r in rows
    ]

def get_property(property_id: int) -> Optional[PropertyResponseDTO]:
    row = repository.find_by_id(property_id)
    if not row:
        return None
    return PropertyResponseDTO(
        id=row["id"],
        address=row["address"],
        city=row["city"],
        price=row["price"],
        description=row.get("description"),
        year=row.get("year"),
        status=row.get("status"),
    )

def create_property(dto: PropertyRequestDTO) -> PropertyResponseDTO:
    new_id = repository.insert_property(
        {
            "address": dto.address,
            "city": dto.city,
            "price": dto.price,
            "description": dto.description,
            "year": dto.year,
        }
    )
    if dto.status:
        repository.append_status_history(new_id, dto.status)
    return get_property(new_id)

def update_property(property_id: int, dto: PropertyUpdateDTO) -> Optional[PropertyResponseDTO]:
    data: Dict = {}
    if dto.address is not None:
        data["address"] = dto.address
    if dto.city is not None:
        data["city"] = dto.city
    if dto.price is not None:
        data["price"] = dto.price
    if dto.description is not None:
        data["description"] = dto.description
    if dto.year is not None:
        data["year"] = dto.year
    if dto.status is not None:
        data["status"] = dto.status

    updated = repository.update_property(property_id, data)
    if updated <= 0:
        return None
    return get_property(property_id)

def delete_property(property_id: int) -> bool:
    deleted = repository.delete_property(property_id)
    return deleted > 0
