# backend/database/db_handler.py
from __future__ import annotations

from contextlib import contextmanager
from typing import Any, Dict, List, Sequence, Type

from database import db


# ------------------- Contexto transaccional -------------------
@contextmanager
def session_scope():
    """
    Uso:
        with session_scope() as session:
            session.add(obj)
            ...
    Hace commit al salir o rollback si hay excepción.
    """
    session = db.session
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


# ------------------------ CRUD genérico ------------------------
class DBHandler:
    """Operaciones básicas y utilidades del e-commerce."""

    # ----- genéricos -----
    @staticmethod
    def add(instance: db.Model) -> db.Model:
        db.session.add(instance)
        db.session.commit()
        return instance

    @staticmethod
    def get_by_id(model: Type[db.Model], obj_id: Any) -> db.Model | None:
        return model.query.get(obj_id)

    @staticmethod
    def get_all(
        model: Type[db.Model],
        filters: Sequence = None,
        order_by=None,
        limit: int | None = None,
    ) -> List[db.Model]:
        query = model.query
        if filters:
            query = query.filter(*filters)
        if order_by is not None:
            query = query.order_by(order_by)
        if limit:
            query = query.limit(limit)
        return query.all()

    @staticmethod
    def update(instance: db.Model, **attrs) -> db.Model:
        for key, value in attrs.items():
            setattr(instance, key, value)
        db.session.commit()
        return instance

    @staticmethod
    def delete(instance: db.Model) -> None:
        db.session.delete(instance)
        db.session.commit()

    # ----- helpers específicos -----
    @staticmethod
    def create_order(user, items: List[Dict[str, Any]]):
        """
        items = [
            {"product": <Product>, "quantity": 2},
            ...
        ]
        Descuenta stock, calcula total y crea Order + OrderItems.
        """
        from models import Order, OrderItem  # import tardío para evitar ciclos

        total = 0
        order = Order(user=user, status="pending")
        db.session.add(order)

        for item in items:
            product = item["product"]
            quantity = item["quantity"]

            # validación de stock
            if product.stock < quantity:
                raise ValueError(f"Stock insuficiente para {product.name}")

            product.stock -= quantity
            price_snapshot = product.price
            total += price_snapshot * quantity

            db.session.add(
                OrderItem(
                    order=order,
                    product=product,
                    quantity=quantity,
                    price=price_snapshot,
                )
            )

        order.total = total
        db.session.commit()
        return order

    @staticmethod
    def get_user_orders(user_id: int):
        from models import Order

        return (
            Order.query.filter_by(user_id=user_id)
            .order_by(Order.created_at.desc())
            .all()
        )
