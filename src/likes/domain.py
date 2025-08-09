from dataclasses import dataclass
from typing import Dict, Tuple, Optional

@dataclass
class Like:
    id: int
    user_id: int
    property_id: int

class FakeLike:
    def __init__(self) -> None:
        self._auto_id: int = 1
        self._by_id: Dict[int, Like] = {}
        self._by_key: Dict[Tuple[int, int], int] = {}

    def exists_id(self, user_id: int, property_id: int) -> Optional[int]:
        return self._by_key.get((user_id, property_id))

    def insert_like(self, user_id: int, property_id: int) -> int:
        like_id = self._auto_id
        self._auto_id += 1
        like = Like(id=like_id, user_id=user_id, property_id=property_id)
        self._by_id[like_id] = like
        self._by_key[(user_id, property_id)] = like_id
        return like_id

    def delete_like(self, like_id: int) -> int:
        like = self._by_id.pop(like_id, None)
        if not like:
            return 0
        self._by_key.pop((like.user_id, like.property_id), None)
        return 1

def toggle_like(store: FakeLike, user_id: int, property_id: int) -> int:
    """Si existe el like, lo elimina y retorna 0. Si no existe, lo crea y retorna el nuevo id."""
    existing = store.exists_id(user_id, property_id)
    if existing:
        store.delete_like(existing)
        return 0
    return store.insert_like(user_id, property_id)


