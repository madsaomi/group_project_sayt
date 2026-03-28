from flask import Flask
from extensions import db
from config import Config
from routes.main import main_bp
from routes.products import products_bp
from routes.transactions import transactions_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(transactions_bp)

    return app

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)
