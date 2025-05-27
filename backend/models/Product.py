from datetime import datetime
from decimal import Decimal
from database import db
from utils.validators import positive_price, positive_int

class Product(db.Model):
    __tablename__ = "products"

    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price       = db.Column(db.Numeric(10, 2), nullable=False, default=Decimal("0.00"))
    stock       = db.Column(db.Integer, nullable=False, default=0)
    created_at  = db.Column(db.DateTime, default=datetime.utcnow)

    order_items = db.relationship("OrderItem", back_populates="product")


    # validación antes de insertar/actualizar
    def clean(self):
        self.price = positive_price(self.price)
        self.stock = positive_int(self.stock)
    
    
    def __repr__(self) -> str:
        return f"<Product {self.name} (${self.price})>"
