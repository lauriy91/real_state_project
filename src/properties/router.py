from typing import List, Tuple

Route = Tuple[str, str, str]

ROUTES: List[Route] = [
    ("GET", "/properties", "src.properties.handlers.list_properties"),
    ("GET", "/properties/{id}", "src.properties.handlers.get_property"),
    ("POST", "/properties", "src.properties.handlers.create_property"),
    ("PATCH", "/properties/{id}", "src.properties.handlers.update_property"),
    ("DELETE", "/properties/{id}", "src.properties.handlers.delete_property"),
]
