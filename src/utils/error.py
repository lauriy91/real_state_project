from http import HTTPStatus
from typing import Tuple, Dict

from src.utils.json_manager import write_json_response

class AppError(Exception):
    status = HTTPStatus.INTERNAL_SERVER_ERROR
    code = "internal_error"

    def __init__(self, message: str | None = None):
        super().__init__(message or self.code)
        self.message = message or self.code

class NotFoundError(AppError):
    status = HTTPStatus.NOT_FOUND
    code = "not_found"

class ServiceUnavailableError(AppError):
    status = HTTPStatus.SERVICE_UNAVAILABLE
    code = "service_unavailable"

def to_http_error(error: Exception) -> Tuple[int, Dict]:
    if isinstance(error, AppError):
        return error.status, {"error": error.code, "message": error.message}
    return HTTPStatus.INTERNAL_SERVER_ERROR, {"error": "internal_error", "message": str(error) or "internal error"}

def write_error(handler, error: Exception) -> None:
    status, payload = to_http_error(error)
    write_json_response(handler, payload, status=status)
