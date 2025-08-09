from typing import Any, Dict, List, Optional, Tuple

from src.db.connection import fetch_all, get_connection


TABLE = "properties"


def find_all(limit: int = 100, offset: int = 0) -> List[Dict]:
    sql = f"""
        SELECT id, status, price, address, city, description, image_url, property_type, property_subtype, property_size
        FROM {TABLE}
        ORDER BY id ASC
        LIMIT %s OFFSET %s
    """
    return fetch_all(sql, (limit, offset))


def find_by_id(property_id: int) -> Optional[Dict]:
    sql = f"""
        SELECT id, status, price, address, city, description, image_url, property_type, property_subtype, property_size
        FROM {TABLE}
        WHERE id = %s
    """
    rows = fetch_all(sql, (property_id,))
    return rows[0] if rows else None


def exists_id(property_id: int, exclude_id: Optional[int] = None) -> bool:
    if exclude_id is None:
        sql = f"SELECT 1 FROM {TABLE} WHERE id = %s LIMIT 1"
        rows = fetch_all(sql, (property_id,))
    else:
        sql = f"SELECT 1 FROM {TABLE} WHERE id = %s AND id <> %s LIMIT 1"
        rows = fetch_all(sql, (property_id, exclude_id))
    return bool(rows)


def insert_property(data: Dict[str, Any]) -> int:
    columns = [
        "status",
        "price",
        "address",
        "city",
        "description",
        "image_url",
        "property_type",
        "property_subtype",
        "property_size",
    ]
    values = [
        data.get("status"),
        data.get("price"),
        data.get("address"),
        data.get("city"),
        data.get("description"),
        data.get("image_url"),
        data.get("property_type"),
        data.get("property_subtype"),
        data.get("property_size"),
    ]
    placeholders = ", ".join(["%s"] * len(columns))
    cols_sql = ", ".join(columns)
    sql = f"INSERT INTO {TABLE} ({cols_sql}) VALUES ({placeholders})"
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, values)
            return int(cur.lastrowid)


def update_property(property_id: int, data: Dict[str, Any]) -> int:
    if not data:
        return 0
    sets: List[str] = []
    params: List[Any] = []
    for key in [
        "status",
        "price",
        "address",
        "city",
        "description",
        "image_url",
        "property_type",
        "property_subtype",
        "property_size",
    ]:
        if key in data:
            sets.append(f"{key} = %s")
            params.append(data[key])
    if not sets:
        return 0
    sql = f"UPDATE {TABLE} SET {', '.join(sets)} WHERE id = %s"
    params.append(property_id)
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            return int(cur.rowcount)


def delete_property(property_id: int) -> int:
    sql = f"DELETE FROM {TABLE} WHERE id = %s"
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (property_id,))
            return int(cur.rowcount)
