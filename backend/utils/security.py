
import jwt, datetime
import functools
from flask import request, jsonify, g
from config.settings import Config
from utils.errors import Unauthorized
from models.User import User
import traceback



def generate_jwt(payload: dict, expires_in: int = Config.JWT_EXPIRES_IN):
    now = datetime.datetime.utcnow()
    payload |= {
        "iat": now,
        "exp": now + datetime.timedelta(seconds=expires_in)
    }
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
                raise Unauthorized("Token requerido")
            try:
                payload = decode_jwt(auth.split()[1])
                user = User.query.get(int(payload["sub"]))
                if user is None:
                    raise ValueError("user not found")
                if admin_only and not user.is_admin:
                    return jsonify({"msg": "Solo admin"}), 403
                g.current_user = user  # 👈 más seguro que usar request.user
            except Exception as e:
                print("⚠️ Error en JWT:", e)
                traceback.print_exc()
                raise Unauthorized("Token inválido")
            return fn(*args, **kwargs)
        return inner
    return wrapper
