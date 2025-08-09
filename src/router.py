import re
from typing import Callable, Dict, List, Optional, Tuple

from src.routes import ROUTES as RAW_ROUTES

CompiledRoute = Tuple[str, "re.Pattern", Callable]

def _pattern_to_regex(pattern: str) -> "re.Pattern":
    # Convierte /users/{id} -> ^/users/(?P<id>[^/]+)$
    regex = re.sub(r"\{(\w+)\}", r"(?P<\1>[^/]+)", pattern)
    return re.compile(f"^{regex}$")

_COMPILED_ROUTES: List[CompiledRoute] = [
    (method, _pattern_to_regex(path), handler) for method, path, handler in RAW_ROUTES
]

def resolve_handler(method: str, path: str) -> Optional[Tuple[Callable, Dict[str, str]]]:
    method = method.upper()
    for m, regex, handler in _COMPILED_ROUTES:
        if m != method:
            continue
        match = regex.match(path)
        if match:
            return handler, match.groupdict()
    return None


