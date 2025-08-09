from http import HTTPStatus

from src.likes.dto import LikeRequestDTO, LikeResponseDTO
from src.likes import service
from src.utils.json_manager import read_json_body, write_json_response
from src.utils.error import NotFoundError, write_error


def create_like(handler):
    data = read_json_body(handler)
    dto = LikeRequestDTO(**data)
    created = service.create_like(dto)
    # Toggle-like: si se eliminó el like existente, retorna 200 con id=0
    status = HTTPStatus.CREATED if created.id != 0 else HTTPStatus.OK
    write_json_response(handler, created.dict(), status=status)


def delete_like(handler, params):
    like_id = int(params["id"])  # viene del router
    ok = service.delete_like(like_id)
    if not ok:
        write_error(handler, NotFoundError("like not found"))
        return
    handler.send_response(HTTPStatus.NO_CONTENT)
    handler.end_headers()
