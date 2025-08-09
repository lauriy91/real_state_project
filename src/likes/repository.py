from typing import Any, Dict, List, Optional, Tuple

from src.db.connection import fetch_all, get_connection


TABLE = "likes"


def exists_id(user_id: int, property_id: int, exclude_id: Optional[int] = None) -> bool:
    if exclude_id is None:
        sql = f"SELECT 1 FROM {TABLE} WHERE user_id = %s AND property_id = %s LIMIT 1"
        rows = fetch_all(sql, (user_id, property_id))
    else:
        sql = f"SELECT 1 FROM {TABLE} WHERE user_id = %s AND property_id = %s AND id <> %s LIMIT 1"
        rows = fetch_all(sql, (user_id, property_id, exclude_id))
    return bool(rows)


def insert_like(data: Dict[str, Any]) -> int:
    columns = [
        "user_id",
        "property_id",
    ]
    values = [
        data.get("user_id"),
        data.get("property_id"),
    ]
    placeholders = ", ".join(["%s"] * len(columns))
    cols_sql = ", ".join(columns)
    sql = f"INSERT INTO {TABLE} ({cols_sql}) VALUES ({placeholders})"
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, values)
            return int(cur.lastrowid)


def insert_dislike(data: Dict[str, Any]) -> int:
    columns = [
        "user_id",
        "property_id",
    ]
    values = [
        data.get("user_id"),
        data.get("property_id"),
    ]
    placeholders = ", ".join(["%s"] * len(columns))
    cols_sql = ", ".join(columns)
    sql = f"INSERT INTO {TABLE} ({cols_sql}) VALUES ({placeholders})"
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, values)
            return int(cur.lastrowid)


def delete_like(like_id: int) -> int:
    sql = f"DELETE FROM {TABLE} WHERE id = %s"
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (like_id,))
            return int(cur.rowcount)
