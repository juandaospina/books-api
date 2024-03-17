from flask import Flask

from .db import db, ma, migrate


def initialize_extensions(app: Flask):
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Config
    app.config.from_object("app.config")
    app.config.from_pyfile("config.py", silent=True)
    print(app.config)

    # Extensions
    initialize_extensions(app)

    with app.app_context():
        db.create_all()

    return app