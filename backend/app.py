from flask import Flask, jsonify
from flask_cors import CORS
from database import db
from config.settings import Config
from api import auth as auth_bp, products as prod_bp, orders as ord_bp  # noqa
from sqlalchemy.exc import IntegrityError
from utils.errors import APIError

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # extensiones
    db.init_app(app)
    CORS(app, origins=Config.CORS_ORIGINS)

    # ---------- MANEJO DE ERRORES ----------
    @app.errorhandler(APIError)
    def handle_api_error(err):
        return jsonify({"error": err.message}), err.status_code

    @app.errorhandler(IntegrityError)
    def handle_integrity(err):
        return jsonify({"error": "Violación de integridad"}), 400

    @app.errorhandler(404)
    def handle_404(_):
        return jsonify({"error": "Recurso no encontrado"}), 404
    
    app.register_error_handler(404, handle_404)

    @app.errorhandler(500)
    def handle_500(err):
        return jsonify({"error": "Error interno"}), 500

    # ---------- ENCABEZADOS DE SEGURIDAD ----------
    @app.after_request
    def set_secure_headers(resp):
        resp.headers["X-Content-Type-Options"] = "nosniff"
        resp.headers["X-Frame-Options"] = "DENY"
        resp.headers["Referrer-Policy"] = "no-referrer"
        resp.headers["Content-Security-Policy"] = "default-src 'self'"
        return resp
    

    # blueprints
    app.register_blueprint(auth_bp.bp_auth)
    app.register_blueprint(prod_bp.bp_products)
    app.register_blueprint(ord_bp.bp_orders)

    @app.route("/ping")
    def ping():
        return {"msg": "pong"}

    return app



if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(port=5000, debug=Config.DEBUG)
