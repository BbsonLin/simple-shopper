from flask import Flask, jsonify
from config import config
from app.extensions import db
from app.modules.product.models import Product


def init_db():
    db.create_all()
    Product.insert_default()
    print('Default products had been created ...')


def create_app(config_name, **kwargs):
    """
    Entry point for the Flask app.
    """
    app = Flask(__name__, template_folder=config[config_name].TEMPLATE_FOLDER,
                static_folder=config[config_name].STATIC_FOLDER, **kwargs)
    app.config.from_object(config[config_name])


    @app.errorhandler(400)
    def handle400(error):
        app.logger.error(error.description)
        response = jsonify(message=error.description)
        return response, 400

    @app.errorhandler(401)
    def handle401(error):
        app.logger.error(error.description)
        response = jsonify(message=error.description)
        return response, 401

    @app.errorhandler(403)
    def handle403(error):
        app.logger.error(error.description)
        response = jsonify(message=error.description)
        return response, 403

    from . import extensions
    extensions.init_app(app)

    from . import modules
    modules.init_app(app)

    return app