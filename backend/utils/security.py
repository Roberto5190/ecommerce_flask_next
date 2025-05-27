from passlib.hash import bcrypt
import jwt, datetime
from config.settings import Config

def hash_password(raw: str) -> str:
    return bcrypt.hash(raw)

def verify_password(raw: str, hashed: str) -> bool:
    return bcrypt.verify(raw, hashed)

def generate_jwt(payload: dict, expires_in: int = Config.JWT_EXPIRES_IN):
    now = datetime.datetime.utcnow()
    payload |= {"iat": now, "exp": now + datetime.timedelta(seconds=expires_in)}
    return jwt.encode(payload, Config.SECRET_KEY, algorithm=Config.JWT_ALGORITHM)
