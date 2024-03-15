from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Config
    app.config.from_object("app.config")
    app.config.from_pyfile("config.py", silent=True)

    print(app.config)
    return app