from flask import Flask
from flask_cors import CORS
from database import db
from config.settings import Config
from api import auth as auth_bp, products as prod_bp, orders as ord_bp  # noqa

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # extensiones
    db.init_app(app)
    CORS(app, origins=Config.CORS_ORIGINS)

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
