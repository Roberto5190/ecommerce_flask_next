from passlib.hash import bcrypt
import jwt, datetime
from config.settings import Config
import functools
from flask import request, jsonify
from models import User

def hash_password(raw: str) -> str:
    return bcrypt.hash(raw)

def verify_password(raw: str, hashed: str) -> bool:
    return bcrypt.verify(raw, hashed)

def generate_jwt(payload: dict, expires_in: int = Config.JWT_EXPIRES_IN):
    now = datetime.datetime.utcnow()
    payload |= {"iat": now, "exp": now + datetime.timedelta(seconds=expires_in)}
    return jwt.encode(payload, Config.SECRET_KEY, algorithm=Config.JWT_ALGORITHM)




def decode_jwt(token: str):
    return jwt.decode(token, Config.SECRET_KEY, algorithms=[Config.JWT_ALGORITHM])

def jwt_required(admin_only: bool = False):
    """Decorador para proteger rutas"""
    def wrapper(fn):
        @functools.wraps(fn)
        def inner(*args, **kwargs):
            auth = request.headers.get("Authorization", "")
            if not auth.startswith("Bearer "):
                return jsonify({"msg": "Token requerido"}), 401
            try:
                payload = decode_jwt(auth.split()[1])
                user = User.query.get(payload["sub"])
                if user is None:
                    raise ValueError("user not found")
                if admin_only and not user.is_admin:
                    return jsonify({"msg": "Solo admin"}), 403
                # inyectamos usuario en el request
                request.user = user
            except Exception:
                return jsonify({"msg": "Token inválido"}), 401
            return fn(*args, **kwargs)
        return inner
    return wrapper