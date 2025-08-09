from typing import Any, List, Sequence
import pymysql
from pymysql.cursors import DictCursor
from src.config.config import get_db_config


def get_connection():
    cfg = get_db_config()
    return pymysql.connect(
        host=cfg.host,
        port=cfg.port,
        user=cfg.user,
        password=cfg.password,
        database=cfg.name,
        cursorclass=DictCursor,
        charset="utf8mb4",
        autocommit=True,
    )


def fetch_all(sql: str, params: Sequence[Any] | None = None) -> List[dict]:
    params = params or ()
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            return list(cur.fetchall())


def execute(sql: str, params: Sequence[Any] | None = None) -> int:
    params = params or ()
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.rowcount
