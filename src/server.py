from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse

from src.router import resolve_handler
from src.utils.error import write_error, ServiceUnavailableError
from src.utils.logger import get_logger

logger = get_logger(__name__)

class AppHandler(BaseHTTPRequestHandler):
    def _dispatch(self, method: str):
        parsed = urlparse(self.path)
        try:
            resolved = resolve_handler(method, parsed.path)
        except Exception as e:
            write_error(self, ServiceUnavailableError(str(e)))
            return

        if not resolved:
            self.send_error(404, "Not Found")
            return

        handler_func, path_params = resolved
        try:
            handler_func(self, **path_params)
        except Exception as e:
            logger.exception("Error handling %s %s", method, parsed.path)
            write_error(self, e)

    def do_GET(self):  # noqa: N802
        self._dispatch("GET")

    def do_POST(self):  # noqa: N802
        self._dispatch("POST")

    def do_PUT(self):  # noqa: N802
        self._dispatch("PUT")

    def do_PATCH(self):  # noqa: N802
        self._dispatch("PATCH")

    def do_DELETE(self):  # noqa: N802
        self._dispatch("DELETE")

    def log_message(self, format: str, *args):  # noqa: A003
        return
