from flask import Flask
from flask_restful import Api
from flask_apispec.extension import APISpec, MarshmallowPlugin

from .db import db, ma, migrate
from app.docs import docs
from app.books.router import books_bp
from app.authors.router import authors_bp
from app.errors_handling import register_errors


def initialize_extensions(app: Flask):
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    docs.init_app(app)


def configure_docs(app: Flask):
    doc_config = {
        'APISPEC_SPEC': APISpec(
            title='Books API',
            version='1.0',
            openapi_version="2.0.0", 
            plugins=[MarshmallowPlugin()],
        ),
        'APISPEC_SWAGGER_URL': '/docs',
        'APISPEC_SWAGGER_UI_URL': '/docs-ui',
    }
    app.config.update(doc_config)


def register_blueprints(app: Flask):
    app.register_blueprint(books_bp)
    app.register_blueprint(authors_bp)


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Config
    app.config.from_object("app.config")
    app.config.from_pyfile("config.py", silent=True)

    Api(app, catch_all_404s=False)

    # Blueprints
    register_blueprints(app)

    # Documentation
    configure_docs(app)

    # Error handling
    register_errors(app)

    # Extensions
    initialize_extensions(app)

    with app.app_context():
        db.create_all()

    return app