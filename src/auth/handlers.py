from http import HTTPStatus

from src.auth.dto import LoginRequestDTO
from src.auth import service
from src.utils.json_manager import read_json_body, write_json_response
from src.utils.error import write_error, AppError


def login(handler):
    data = read_json_body(handler)
    dto = LoginRequestDTO(**data)
    try:
        resp = service.login(dto)
    except service.InvalidCredentialsError as e:
        write_error(handler, AppError(str(e)))
        return
    write_json_response(handler, resp.dict(), status=HTTPStatus.OK)


def logout(handler):
    write_json_response(handler, {"ok": True}, status=HTTPStatus.OK)


