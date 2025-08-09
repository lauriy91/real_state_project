from typing import Callable, List, Tuple, Any
import importlib

from src.users.router import ROUTES as USER_ROUTES
from src.properties.router import ROUTES as PROPERTY_ROUTES
from src.likes.router import ROUTES as LIKE_ROUTES

RawRoute = Tuple[str, str, Any]
Route = Tuple[str, str, Callable]

def _to_callable(ref: Any) -> Callable:
    if callable(ref):
        return ref
    if isinstance(ref, str):
        module_name, func_name = ref.rsplit(".", 1)
        mod = importlib.import_module(module_name)
        return getattr(mod, func_name)
    raise TypeError("Invalid route handler reference")

def _normalize_routes(raw_routes: List[RawRoute]) -> List[Route]:
    normalized: List[Route] = []
    for method, path, handler_ref in raw_routes:
        normalized.append((method.upper(), path, _to_callable(handler_ref)))
    return normalized

ROUTES: List[Route] = _normalize_routes([
    *USER_ROUTES,
    *PROPERTY_ROUTES,
    *LIKE_ROUTES,
])
