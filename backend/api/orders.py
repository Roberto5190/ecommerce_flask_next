from flask import Blueprint, request, jsonify, g
from database import DBHandler
from models import Product
from utils.security import jwt_required
from utils.errors import APIError

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
    
    try:
        order = DBHandler.create_order(g.current_user, parsed)
        return jsonify({"order_id": order.id}), 201
    except ValueError as e:
        # error de negocio → 400 Bad Request
        raise APIError(str(e), status_code=400)


@bp_orders.get("/")
@jwt_required()
def my_orders():
    orders = DBHandler.get_user_orders(g.current_user.id)
    return jsonify([{
        "id": o.id,
        "total": float(o.total),
        "status": o.status,
        "created_at": o.created_at.isoformat(),
        "items": [{"product_id": i.product_id, "qty": i.quantity} for i in o.items],
    } for o in orders])
