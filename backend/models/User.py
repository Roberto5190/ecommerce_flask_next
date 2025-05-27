from datetime import datetime
from database import db

class User(db.Model):
    __tablename__ = "users"

    id          = db.Column(db.Integer, primary_key=True)
    username    = db.Column(db.String(50), unique=True, nullable=False)
    email       = db.Column(db.String(120), unique=True, nullable=False)
    password    = db.Column(db.String(255), nullable=False)      # hash
    is_admin    = db.Column(db.Boolean, default=False)
    created_at  = db.Column(db.DateTime, default=datetime.utcnow)

    orders      = db.relationship("Order", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<User {self.username}>"
