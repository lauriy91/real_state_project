from typing import List, Tuple

Route = Tuple[str, str, str]

ROUTES: List[Route] = [
    ("POST", "/likes", "src.likes.handlers.create_like"),
    ("POST", "/dislikes", "src.likes.handlers.create_dislike"),
    ("DELETE", "/likes/{id}", "src.likes.handlers.delete_like"),
]
