from flask import Flask
from sqlalchemy import inspect          
from database import db
from models import User, Product, Order, OrderItem

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db.init_app(app)

with app.app_context():
    db.create_all()
    inspector = inspect(db.engine)
    print("✓ Tablas creadas en memoria:", inspector.get_table_names())
