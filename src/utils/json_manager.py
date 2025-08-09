import json
from http import HTTPStatus
from typing import Dict

def read_json_body(request) -> Dict:
    length = int(request.headers.get("Content-Length", 0))
    if length <= 0:
        return {}
    raw = request.rfile.read(length)
    try:
        return json.loads(raw.decode("utf-8"))
    except Exception:
        return {}

def write_json_response(handler, payload, status=HTTPStatus.OK):
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)