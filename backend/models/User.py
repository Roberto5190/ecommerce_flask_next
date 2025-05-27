from datetime import datetime
from database import db
from utils.validators import email as validate_email, password_strength
from utils.security import hash_password, verify_password



class User(db.Model):
    __tablename__ = "users"

    id          = db.Column(db.Integer, primary_key=True)
    username    = db.Column(db.String(50), unique=True, nullable=False)
    email       = db.Column(db.String(120), unique=True, nullable=False)
    password    = db.Column(db.String(255), nullable=False)      # hash
    is_admin    = db.Column(db.Boolean, default=False)
    created_at  = db.Column(db.DateTime, default=datetime.utcnow)

    orders      = db.relationship("Order", back_populates="user", cascade="all, delete-orphan")


    # --------- factory helpers ----------
    @classmethod
    def create(cls, username: str, email: str, raw_password: str, **extras):
        validate_email(email)
        password_strength(raw_password)
        return cls(
            username=username,
            email=email.lower(),
            password=hash_password(raw_password),
            **extras,
        )

    # --------- instancia ----------
    def check_password(self, raw: str) -> bool:
        return verify_password(raw, self.password)


    def __repr__(self) -> str:
        return f"<User {self.username}>"
