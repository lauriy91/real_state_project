from http import HTTPStatus

from src.users.dto import UserRequestDTO, UserUpdateDTO
from src.users import service
from src.utils.json_manager import read_json_body, write_json_response
from src.utils.error import NotFoundError, write_error

def list_users(handler):
    items = [u.dict() for u in service.list_users()]
    write_json_response(handler, {"items": items})

def get_user(handler, params):
    user_id = int(params["id"])  # veine del router
    found = service.get_user(user_id)
    if not found:
        write_error(handler, NotFoundError("user not found"))
        return
    write_json_response(handler, found.dict())

def create_user(handler):
    data = read_json_body(handler)
    dto = UserRequestDTO(**data)
    created = service.create_user(dto)
    write_json_response(handler, created.dict(), status=HTTPStatus.CREATED)

def update_user(handler, params):
    user_id = int(params["id"])  # veine del router
    data = read_json_body(handler)
    dto = UserUpdateDTO(**data)
    updated = service.update_user(user_id, dto)
    if not updated:
        write_error(handler, NotFoundError("user not found"))
        return
    write_json_response(handler, updated.dict())

def delete_user(handler, params):
    user_id = int(params["id"])  # veine del router
    ok = service.delete_user(user_id)
    if not ok:
        write_error(handler, NotFoundError("user not found"))
        return
    handler.send_response(HTTPStatus.NO_CONTENT)
    handler.end_headers()
