from flask import Blueprint, request, jsonify
from database import DBHandler
from models import Product
from utils.security import jwt_required

bp_products = Blueprint("products", __name__, url_prefix="/api/products")

@bp_products.get("/")
def list_products():
    prods = Product.query.all()
    return jsonify([{
        "id": p.id, "name": p.name, "price": float(p.price),
        "stock": p.stock
    } for p in prods])

@bp_products.get("/<int:prod_id>")
def get_product(prod_id):
    p = Product.query.get_or_404(prod_id)
    return jsonify({
        "id": p.id, "name": p.name, "description": p.description,
        "price": float(p.price), "stock": p.stock
    })

@bp_products.post("/")
@jwt_required(admin_only=True)
def create_product():
    data = request.get_json()
    try:
        prod = Product(**data)
        prod.clean()
        DBHandler.add(prod)
        return jsonify({"id": prod.id}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
