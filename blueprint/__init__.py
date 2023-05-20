from flask import Flask
# from flask.templating import render_template
from flask import render_template
from flask import flash, redirect, url_for
import os, yaml
# from .extensions import api

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    print(f"debug: {app.config['DEBUG']}")

    if test_config is None:
        if(app.config["DEBUG"] == True):
            config_file = os.path.join(app.instance_path, 'development.yaml')
            app.config.from_file(config_file, load=yaml.safe_load)
    print(f"\napp.config['DATABASE_USER']: {app.config['DATABASE_USER']}\napp.config['DATABASE_ENGINE']: {app.config['DATABASE_ENGINE']}")


    # from .product import product as product_blueprint
    # app.register_blueprint(product_blueprint)

    from .extension import db, api
    db.init_app(app)
    api.init_app(app)
    from .resource import ns
    api.add_namespace(ns)

    from . import model
    model.init_app(app)


    return app