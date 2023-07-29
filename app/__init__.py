from flask import Flask
from flask_cors import CORS
from config import Config
from app.extensions import db
from app.routes import api_bp


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app)

    # Initialize Flask extensions here
    db.init_app(app)

    # Register blueprints here
    app.register_blueprint(api_bp, url_prefix='/api')

    return app

