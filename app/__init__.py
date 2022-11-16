from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.config.from_object(Config)

    SQLAlchemy(app)

    return app
