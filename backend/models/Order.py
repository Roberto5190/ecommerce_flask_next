from datetime import datetime
from decimal import Decimal
from database import db


ALLOWED_STATUS = {"pending", "paid", "shipped", "completed", "cancelled"}

class Order(db.Model):
    __tablename__ = "orders"

    id          = db.Column(db.Integer, primary_key=True)
    user_id     = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    total       = db.Column(db.Numeric(10, 2), nullable=False, default=Decimal("0.00"))
    status      = db.Column(db.String(20), nullable=False, default="pending")
    created_at  = db.Column(db.DateTime, default=datetime.utcnow)

    user        = db.relationship("User", back_populates="orders")
    items       = db.relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")

    # setter con validación
    def set_status(self, new_status: str):
        if new_status not in ALLOWED_STATUS:
            raise ValueError(f"Estado '{new_status}' no permitido")
        self.status = new_status

    def __repr__(self) -> str:
        return f"<Order {self.id} – {self.status}>"



class OrderItem(db.Model):
    __tablename__ = "order_items"

    id          = db.Column(db.Integer, primary_key=True)
    order_id    = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False)
    product_id  = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    quantity    = db.Column(db.Integer, nullable=False, default=1)
    price       = db.Column(db.Numeric(10, 2), nullable=False)   # precio en el momento de la compra

    order       = db.relationship("Order", back_populates="items")
    product     = db.relationship("Product", back_populates="order_items")

    def __repr__(self) -> str:
        return f"<Item {self.product_id} x{self.quantity}>"
