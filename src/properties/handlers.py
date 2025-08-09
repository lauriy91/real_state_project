from http import HTTPStatus

from src.properties.dto import PropertyRequestDTO, PropertyUpdateDTO
from src.properties import service
from src.utils.json_manager import read_json_body, write_json_response
from src.utils.error import NotFoundError, write_error

def list_properties(handler):
    # filtros: status (múltiple), city, year_from, year_to
    from urllib.parse import urlparse, parse_qs

    parsed = urlparse(handler.path)
    qs = parse_qs(parsed.query)
    status = qs.get("status")
    city = qs.get("city", [None])[0]
    year_from = qs.get("year_from", [None])[0]
    year_to = qs.get("year_to", [None])[0]

    filters = {
        "status": status,
        "city": city,
        "year_from": int(year_from) if year_from and year_from.isdigit() else None,
        "year_to": int(year_to) if year_to and year_to.isdigit() else None,
    }

    items = [p.dict() for p in service.list_properties(filters=filters)]
    write_json_response(handler, {"items": items})


def get_property(handler, params):
    property_id = int(params["id"])  # viene del router
    found = service.get_property(property_id)
    if not found:
        write_error(handler, NotFoundError("property not found"))
        return
    write_json_response(handler, found.dict())

def create_property(handler):
    data = read_json_body(handler)
    dto = PropertyRequestDTO(**data)
    created = service.create_property(dto)
    write_json_response(handler, created.dict(), status=HTTPStatus.CREATED)

def update_property(handler, params):
    property_id = int(params["id"])  # viene del router
    data = read_json_body(handler)
    dto = PropertyUpdateDTO(**data)
    updated = service.update_property(property_id, dto)
    if not updated:
        write_error(handler, NotFoundError("property not found"))
        return
    write_json_response(handler, updated.dict())

def delete_property(handler, params):
    property_id = int(params["id"])  # viene del router
    ok = service.delete_property(property_id)
    if not ok:
        write_error(handler, NotFoundError("property not found"))
        return
    handler.send_response(HTTPStatus.NO_CONTENT)
    handler.end_headers()
