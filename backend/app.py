
from flask import Flask
from database import db
from models import User, Product

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db.init_app(app)

with app.app_context():
    db.create_all()

    # usuario con pwd en claro → debe hash-earse
    u = User.create("carlos", "carlos@correo.com", "supersecreto")
    db.session.add(u); db.session.commit()
    assert u.check_password("supersecreto") is True
    assert u.password.startswith("$2b$"), "No se hashéo con bcrypt"

    # producto con precio negativo → debe lanzar error
    from decimal import Decimal
    try:
        p = Product(name="Prueba", price=Decimal("-1.00"), stock=5)
        p.clean()
    except ValueError as e:
        print("✓ Validación capturada:", e)

    print("✓ Checkpoint completado sin tracebacks")
