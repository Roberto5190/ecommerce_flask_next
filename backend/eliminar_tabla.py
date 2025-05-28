
from flask import Flask
from database import db
from models import User
from config.settings import Config

# Crear instancia de Flask (si no usas app factory)
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    print("Eliminando tabla 'users'...")
    User.__table__.drop(db.engine, checkfirst=True)

    print("Recreando tabla 'users'...")
    User.__table__.create(db.engine, checkfirst=True)

    print("Tabla 'users' reiniciada con éxito.")
