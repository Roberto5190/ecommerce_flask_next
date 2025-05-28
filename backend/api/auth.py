from flask import Blueprint, request, jsonify
from database import DBHandler
from models import User
from utils.security import generate_jwt

bp_auth = Blueprint("auth", __name__, url_prefix="/api/auth")

@bp_auth.post("/register")
def register():
    data = request.get_json()
    try:
        user = User.create(
            username=data["username"],
            email=data["email"],
            raw_password=data["password"],
        )
        DBHandler.add(user)
        return jsonify({"msg": "Registro ok"}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@bp_auth.post("/login")
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data["email"].lower()).first()
    if not user or not user.check_password(data["password"]):
        return jsonify({"msg": "Credenciales incorrectas"}), 401
    token = generate_jwt({"sub": user.id, "username": user.username})
    return jsonify({"token": token})
