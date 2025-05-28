# scripts/check_user.py

from flask import Flask
from config.settings import Config
from database import db
from models import User

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    print("📌 Verificando si existe el usuario con ID 1...")
    user = User.query.get(1)
    if user:
        print(f"✅ Usuario encontrado: {user.username} | Admin: {user.is_admin}")
    else:
        print("❌ No existe ningún usuario con ID 1.")

    print("\n📋 Lista de todos los usuarios:")
    users = User.query.all()
    for u in users:
        print(f"- ID: {u.id} | Username: {u.username} | Email: {u.email} | Admin: {u.is_admin}")
