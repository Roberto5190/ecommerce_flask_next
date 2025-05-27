from flask import Flask
from database import db, DBHandler
from models import User, Product

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db.init_app(app)

with app.app_context():
    db.create_all()

    user = DBHandler.add(User(username="bob", email="bob@example.com", password="hash"))
    pen  = DBHandler.add(Product(name="Bolígrafo", price=1.5, stock=20))
    order = DBHandler.create_order(user=user, items=[{"product": pen, "quantity": 3}])

    print("Pedido:", order)
    print("Items :", order.items)
    print("Stock restante:", pen.stock)