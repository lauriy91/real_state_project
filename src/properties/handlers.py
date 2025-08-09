from http import HTTPStatus

from src.properties.dto import (
    PropertyRequestDTO,
    PropertyUpdateDTO,
    PropertyResponseDTO,
)
from src.utils.json_manager import read_json_body, write_json_response


def list_properties(handler):
    # building
    write_json_response(handler, {"items": []})


def get_property(handler, params):
    property_id = int(params["id"])
    # building
    write_json_response(handler, {"id": property_id})


def create_property(handler):
    data = read_json_body(handler)
    dto = PropertyRequestDTO(**data)
    # building
    created = PropertyResponseDTO(
        id=1,
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
    write_json_response(handler, created.dict(), status=HTTPStatus.CREATED)


def update_property(handler, params):
    user_id = int(params["id"])
    data = read_json_body(handler)
    dto = PropertyUpdateDTO(**data)
    # building
    updated = PropertyResponseDTO(
        id=user_id,
        status=dto.status or "",
        price=dto.price or "",
        address=dto.address or "",
        city=dto.city or "",
        description=dto.description or "",
        image_url=dto.image_url or "",
        property_type=dto.property_type or "",
        property_subtype=dto.property_subtype or "",
        property_size=dto.property_size or "",
    )
    write_json_response(handler, updated.dict())


def delete_property(handler, params):
    user_id = int(params["id"])
    #  building
    handler.send_response(HTTPStatus.NO_CONTENT)
    handler.end_headers()
