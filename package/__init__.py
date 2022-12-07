from flask import Flask
from flask_wtf.csrf import CSRFProtect


def create_app():
    app = Flask(__name__)
    from .website import website_print
    app.register_blueprint(website_print, url_prefix='/')
    return app
