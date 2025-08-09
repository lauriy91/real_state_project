from typing import Optional, Dict

from src.db.connection import fetch_all, get_connection


def find_user_by_email(email: str) -> Optional[Dict]:
    sql = "SELECT id, username, email, password, is_active FROM auth_user WHERE email = %s LIMIT 1"
    rows = fetch_all(sql, (email,))
    return rows[0] if rows else None


def insert_auth_user(username: str, email: str, password_hash: str) -> int:
    sql = (
        "INSERT INTO auth_user (username, email, password, is_active, is_staff, is_superuser, date_joined)"
        " VALUES (%s, %s, %s, 1, 0, 0, NOW())"
    )
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (username, email, password_hash))
            return int(cur.lastrowid)


