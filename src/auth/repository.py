from typing import Optional, Dict

from src.db.connection import fetch_all

def find_user_by_email(email: str) -> Optional[Dict]:
    sql = "SELECT id, name, email, password FROM users WHERE email = %s LIMIT 1"
    rows = fetch_all(sql, (email,))
    return rows[0] if rows else None


