import os
from dataclasses import dataclass

@dataclass(frozen=True)
class DBConfig:
    host: str
    port: int
    name: str
    user: str
    password: str

def get_db_config() -> DBConfig:
    host = os.getenv("DB_HOST", "localhost")
    port = int(os.getenv("DB_PORT", "3306"))
    name = os.getenv("DB_NAME", "habi")
    user = os.getenv("DB_USER", "root")
    password = os.getenv("DB_PASSWORD", "")
    return DBConfig(host=host, port=port, name=name, user=user, password=password)
