from http import HTTPStatus

from src.likes.dto import LikeRequestDTO, DislikeRequestDTO, LikeResponseDTO
from src.utils.json_manager import read_json_body, write_json_response


def create_like(handler):
    data = read_json_body(handler)
    dto = LikeRequestDTO(**data)
    # building
    created = LikeResponseDTO(id=1, user_id=dto.user_id, property_id=dto.property_id)
    write_json_response(handler, created.dict(), status=HTTPStatus.CREATED)


def create_dislike(handler):
    data = read_json_body(handler)
    dto = DislikeRequestDTO(**data)
    # building
    created = LikeResponseDTO(id=1, user_id=dto.user_id, property_id=dto.property_id)
    write_json_response(handler, created.dict(), status=HTTPStatus.CREATED)


def delete_like(handler, params):
    like_id = int(params["id"])
    #  building
    handler.send_response(HTTPStatus.NO_CONTENT)
    handler.end_headers()
