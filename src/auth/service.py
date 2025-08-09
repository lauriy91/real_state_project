import os
import time
import bcrypt
import jwt

from src.auth.dto import (
    LoginRequestDTO,
    LoginResponseDTO,
    SignupRequestDTO,
    SignupResponseDTO,
)
from src.auth import repository

class InvalidCredentialsError(ValueError):
    pass

def _verify_password(plain: str, hashed: str) -> bool:
    try:
        return bcrypt.checkpw(plain.encode(), hashed.encode())
    except Exception:
        return False

def _create_access_token(user_id: int) -> str:
    secret = os.getenv("AUTH_SECRET", "devsecret")
    ttl = int(os.getenv("AUTH_TTL", "3600"))
    payload = {"sub": user_id, "exp": int(time.time()) + ttl}
    return jwt.encode(payload, secret, algorithm="HS256")

def login(dto: LoginRequestDTO) -> LoginResponseDTO:
    user = repository.find_user_by_email(dto.email)
    if not user:
        raise InvalidCredentialsError("invalid credentials")

    if not _verify_password(dto.password, user["password"]):
        raise InvalidCredentialsError("invalid credentials")

    token = _create_access_token(user_id=user["id"])
    return LoginResponseDTO(access_token=token)

def logout(token: str) -> bool:
    return True

def hash_password(plain: str) -> str:
    return bcrypt.hashpw(plain.encode(), bcrypt.gensalt()).decode()

def signup(dto: SignupRequestDTO) -> SignupResponseDTO:
    pwd_hash = hash_password(dto.password)
    user_id = repository.insert_auth_user(dto.username, dto.email, pwd_hash)
    return SignupResponseDTO(id=user_id, username=dto.username, email=dto.email)
