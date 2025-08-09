from typing import Any, Dict, List, Optional, Tuple

from src.db.connection import fetch_all, get_connection

TABLE = "property"
ALLOWED_VISIBLE_STATUSES = ("pre_venta", "en_venta", "vendido")

def _base_select() -> str:
    return f"""
        SELECT p.id, p.address, p.city, p.price, p.description, p.year,
               s.name AS status
        FROM {TABLE} p
        LEFT JOIN (
          SELECT sh.property_id, sh.status_id
          FROM status_history sh
          JOIN (
            SELECT property_id, MAX(update_date) AS max_ud
            FROM status_history
            GROUP BY property_id
          ) mx
          ON mx.property_id = sh.property_id AND mx.max_ud = sh.update_date
        ) sh ON sh.property_id = p.id
        LEFT JOIN status s ON s.id = sh.status_id
    """

def _filters_where(filters: Optional[Dict[str, Any]]) -> Tuple[str, List[Any]]:
    clauses: List[str] = []
    params: List[Any] = []

    statuses: List[str] = list(ALLOWED_VISIBLE_STATUSES)
    if filters and filters.get("status"):
        requested = [s for s in filters["status"] if s in ALLOWED_VISIBLE_STATUSES]
        if requested:
            statuses = requested
    placeholders = ", ".join(["%s"] * len(statuses))
    clauses.append(f"s.name IN ({placeholders})")
    params.extend(statuses)

    if filters:
        if city := filters.get("city"):
            clauses.append("p.city = %s")
            params.append(city)
        if yf := filters.get("year_from"):
            clauses.append("p.year >= %s")
            params.append(yf)
        if yt := filters.get("year_to"):
            clauses.append("p.year <= %s")
            params.append(yt)

    where_sql = " WHERE " + " AND ".join(clauses) if clauses else ""
    return where_sql, params


def find_all(limit: int = 100, offset: int = 0, filters: Optional[Dict[str, Any]] = None) -> List[Dict]:
    where_sql, params = _filters_where(filters)
    sql = _base_select() + where_sql + " ORDER BY p.id ASC LIMIT %s OFFSET %s"
    params.extend([limit, offset])
    return fetch_all(sql, params)

def find_by_id(property_id: int) -> Optional[Dict]:
    sql = _base_select() + " WHERE p.id = %s"
    rows = fetch_all(sql, (property_id,))
    return rows[0] if rows else None

def insert_property(data: Dict[str, Any]) -> int:
    columns = ["address", "city", "price", "description", "year"]
    values = [
        data.get("address"),
        data.get("city"),
        data.get("price"),
        data.get("description"),
        data.get("year"),
    ]
    placeholders = ", ".join(["%s"] * len(columns))
    cols_sql = ", ".join(columns)
    sql = f"INSERT INTO {TABLE} ({cols_sql}) VALUES ({placeholders})"
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, values)
            new_id = int(cur.lastrowid)
            return new_id

def append_status_history(property_id: int, status_name: str) -> None:
    # inserción por nombre de status
    sql_status = "SELECT id FROM status WHERE name = %s LIMIT 1"
    rows = fetch_all(sql_status, (status_name,))
    if not rows:
        return
    status_id = rows[0]["id"]
    sql_ins = (
        "INSERT INTO status_history (property_id, status_id, update_date) VALUES (%s, %s, NOW())"
    )
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql_ins, (property_id, status_id))

def update_property(property_id: int, data: Dict[str, Any]) -> int:
    if not data:
        return 0
    sets: List[str] = []
    params: List[Any] = []
    for key in ["address", "city", "price", "description", "year"]:
        if key in data:
            sets.append(f"{key} = %s")
            params.append(data[key])
    if sets:
        sql = f"UPDATE {TABLE} SET {', '.join(sets)} WHERE id = %s"
        params.append(property_id)
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, params)
    # si viene status, agregar a history
    if "status" in data and data["status"]:
        append_status_history(property_id, data["status"])
    return 1

def delete_property(property_id: int) -> int:
    sql = f"DELETE FROM {TABLE} WHERE id = %s"
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (property_id,))
            return int(cur.rowcount)
