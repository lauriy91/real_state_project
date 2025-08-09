import logging
import os
from typing import Optional

# Niveles disponibles
_LEVELS = {
    "CRITICAL": logging.CRITICAL,
    "ERROR": logging.ERROR,
    "WARNING": logging.WARNING,
    "INFO": logging.INFO,
    "DEBUG": logging.DEBUG,
}

_level_name = (os.getenv("LOG_LEVEL") or "INFO").upper()
_level = _LEVELS.get(_level_name, logging.INFO)
logging.basicConfig(level=_level, format="[%(levelname)s] %(message)s")

def get_logger(name: Optional[str] = None) -> logging.Logger:
    # Devuelve un logger simple. Uso: logger = get_logger(__name__)
    return logging.getLogger(name or "app")

def set_log_level(level_name: str) -> int:
    # Cambia el nivel global en caliente. Retorna el nivel efectivo.
    level = _LEVELS.get(level_name.upper(), logging.INFO)
    logging.getLogger().setLevel(level)
    return level
