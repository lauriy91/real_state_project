from http.server import HTTPServer

from src.server import AppHandler
from src.utils.logger import get_logger

logger = get_logger(__name__)


def run(host: str = "0.0.0.0", port: int = 8000) -> None:
    httpd = HTTPServer((host, port), AppHandler)
    logger.info("Server listening on http://%s:%s", host, port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()


if __name__ == "__main__":
    run()
