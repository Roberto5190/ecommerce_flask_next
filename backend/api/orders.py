from flask import Blueprint, request, jsonify
from database import DBHandler
from models import Product
from utils.security import jwt_required

bp_orders = Blueprint("orders", __name__, url_prefix="/api/orders")

@bp_orders.post("/")
@jwt_required()
def create_order():
    items = request.get_json().get("items", [])
    # items = [{"product_id": 1, "quantity": 2}, ...]
    parsed = []
    for it in items:
        prod = Product.query.get_or_404(it["product_id"])
        parsed.append({"product": prod, "quantity": it["quantity"]})
    order = DBHandler.create_order(request.user, parsed)
    return jsonify({"order_id": order.id}), 201

@bp_orders.get("/")
@jwt_required()
def my_orders():
    orders = DBHandler.get_user_orders(request.user.id)
    return jsonify([{
        "id": o.id,
        "total": float(o.total),
        "status": o.status,
        "created_at": o.created_at.isoformat(),
        "items": [{"product_id": i.product_id, "qty": i.quantity} for i in o.items],
    } for o in orders])
