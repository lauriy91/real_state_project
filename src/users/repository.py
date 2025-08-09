from typing import Any, Dict, List, Optional, Tuple

from src.db.connection import fetch_all, get_connection


TABLE = "users"


def find_all(limit: int = 100, offset: int = 0) -> List[Dict]:
    sql = f"""
        SELECT id, name, email, city, phone, active
        FROM {TABLE}
        ORDER BY id ASC
        LIMIT %s OFFSET %s
    """
    return fetch_all(sql, (limit, offset))


def find_by_id(user_id: int) -> Optional[Dict]:
    sql = f"""
        SELECT id, name, email, city, phone, active
        FROM {TABLE}
        WHERE id = %s
    """
    rows = fetch_all(sql, (user_id,))
    return rows[0] if rows else None


def exists_email(email: str, exclude_id: Optional[int] = None) -> bool:
    if exclude_id is None:
        sql = f"SELECT 1 FROM {TABLE} WHERE email = %s LIMIT 1"
        rows = fetch_all(sql, (email,))
    else:
        sql = f"SELECT 1 FROM {TABLE} WHERE email = %s AND id <> %s LIMIT 1"
        rows = fetch_all(sql, (email, exclude_id))
    return bool(rows)


def insert_user(data: Dict[str, Any]) -> int:
    columns = ["name", "email", "password", "city", "phone", "active"]
    values = [data.get("name"), data.get("email"), data.get("password"), data.get("city"), data.get("phone"), data.get("active", True)]
    placeholders = ", ".join(["%s"] * len(columns))
    cols_sql = ", ".join(columns)
    sql = f"INSERT INTO {TABLE} ({cols_sql}) VALUES ({placeholders})"
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, values)
            return int(cur.lastrowid)


def update_user(user_id: int, data: Dict[str, Any]) -> int:
    if not data:
        return 0
    sets: List[str] = []
    params: List[Any] = []
    for key in ["name", "email", "password", "city", "phone", "active"]:
        if key in data:
            sets.append(f"{key} = %s")
            params.append(data[key])
    if not sets:
        return 0
    sql = f"UPDATE {TABLE} SET {', '.join(sets)} WHERE id = %s"
    params.append(user_id)
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            return int(cur.rowcount)


def delete_user(user_id: int) -> int:
    sql = f"DELETE FROM {TABLE} WHERE id = %s"
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (user_id,))
            return int(cur.rowcount)
