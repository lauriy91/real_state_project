from http import HTTPStatus

from src.users.dto import UserRequestDTO, UserUpdateDTO, UserResponseDTO
from src.utils.json_manager import read_json_body, write_json_response


def list_users(handler):
    # building
    write_json_response(handler, {"items": []})


def get_user(handler, params):
    user_id = int(params["id"])
    # building
    write_json_response(handler, {"id": user_id})


def create_user(handler):
    data = read_json_body(handler)
    dto = UserRequestDTO(**data)
    # building
    created = UserResponseDTO(
        id=1, name=dto.name, email=dto.email, city=dto.city, phone=dto.phone
    )
    write_json_response(handler, created.dict(), status=HTTPStatus.CREATED)


def update_user(handler, params):
    user_id = int(params["id"])
    data = read_json_body(handler)
    dto = UserUpdateDTO(**data)
    # building
    updated = UserResponseDTO(
        id=user_id,
        name=dto.name or "",
        email=dto.email or "",
        city=dto.city,
        phone=dto.phone or "",
    )
    write_json_response(handler, updated.dict())


def delete_user(handler, params):
    user_id = int(params["id"])
    #  building
    handler.send_response(HTTPStatus.NO_CONTENT)
    handler.end_headers()
