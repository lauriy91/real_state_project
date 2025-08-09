from typing import List, Tuple

Route = Tuple[str, str, str]

ROUTES: List[Route] = [
    ("GET", "/users", "src.users.handlers.list_users"),
    ("GET", "/users/{id}", "src.users.handlers.get_user"),
    ("POST", "/users", "src.users.handlers.create_user"),
    ("PATCH", "/users/{id}", "src.users.handlers.update_user"),
    ("DELETE", "/users/{id}", "src.users.handlers.delete_user"),
]
