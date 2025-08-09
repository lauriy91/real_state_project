from typing import Dict, List, Optional

from src.properties.dto import (
    PropertyRequestDTO,
    PropertyUpdateDTO,
    PropertyResponseDTO,
)
from src.properties import repository


def list_properties(limit: int = 20, offset: int = 0) -> List[PropertyResponseDTO]:
    rows = repository.find_all(limit=limit, offset=offset)
    return [
        PropertyResponseDTO(
            id=r["id"],
            status=r["status"],
            price=r["price"],
            address=r["address"],
            city=r["city"],
            description=r["description"],
            image_url=r["image_url"],
            property_type=r["property_type"],
            property_subtype=r["property_subtype"],
            property_size=r["property_size"],
        )
        for r in rows
    ]


def get_property(property_id: int) -> Optional[PropertyResponseDTO]:
    row = repository.find_by_id(property_id)
    if not row:
        return None
    return PropertyResponseDTO(
        id=row["id"],
        status=row["status"],
        price=row["price"],
        address=row["address"],
        city=row["city"],
        description=row["description"],
        image_url=row["image_url"],
        property_type=row["property_type"],
        property_subtype=row["property_subtype"],
        property_size=row["property_size"],
    )


def create_property(dto: PropertyRequestDTO) -> PropertyResponseDTO:
    if repository.exists_id(dto.id):
        raise ValueError("ID ya registrado")
    new_id = repository.insert_property(
        {
            "status": dto.status,
            "price": dto.price,
            "address": dto.address,
            "city": dto.city,
            "description": dto.description,
            "image_url": dto.image_url,
            "property_type": dto.property_type,
            "property_subtype": dto.property_subtype,
            "property_size": dto.property_size,
        }
    )
    return PropertyResponseDTO(
        id=new_id,
        status=dto.status,
        price=dto.price,
        address=dto.address,
        city=dto.city,
        description=dto.description,
        image_url=dto.image_url,
        property_type=dto.property_type,
        property_subtype=dto.property_subtype,
        property_size=dto.property_size,
    )


def update_property(
    property_id: int, dto: PropertyUpdateDTO
) -> Optional[PropertyResponseDTO]:
    data: Dict = {}
    if dto.status is not None:
        data["status"] = dto.status
    if dto.price is not None:
        data["price"] = dto.price
    if dto.address is not None:
        data["address"] = dto.address
    if dto.city is not None:
        data["city"] = dto.city
    if dto.description is not None:
        data["description"] = dto.description
    if dto.image_url is not None:
        data["image_url"] = dto.image_url
    if dto.property_type is not None:
        data["property_type"] = dto.property_type

    updated = repository.update_property(property_id, data)
    if updated <= 0:
        return None
    return get_property(property_id)


def delete_property(property_id: int) -> bool:
    deleted = repository.delete_property(property_id)
    return deleted > 0
