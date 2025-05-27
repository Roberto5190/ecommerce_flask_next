import re
from decimal import Decimal

EMAIL_RE = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$")

def email(email: str) -> str:
    if not EMAIL_RE.fullmatch(email):
        raise ValueError("Correo inválido")
    return email.lower()

def password_strength(pwd: str) -> str:
    if len(pwd) < 8:
        raise ValueError("La contraseña debe tener ≥ 8 caracteres")
    return pwd

def positive_price(value) -> Decimal:
    from decimal import Decimal
    v = Decimal(value)
    if v < 0:
        raise ValueError("El precio no puede ser negativo")
    return v

def positive_int(value: int) -> int:
    v = int(value)
    if v < 0:
        raise ValueError("El valor no puede ser negativo")
    return v
