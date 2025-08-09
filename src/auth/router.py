from typing import List, Tuple

Route = Tuple[str, str, str]

ROUTES: List[Route] = [
    ("POST", "/signup", "src.auth.handlers.signup"),
    ("POST", "/login", "src.auth.handlers.login"),
    ("POST", "/logout", "src.auth.handlers.logout"),
]


