from flask import Flask
# from flask.templating import render_template
from flask import render_template
from flask import flash, redirect, url_for
import os, yaml

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    if test_config is None:
        if(app.config["ENV"] == "development"):
            config_file = os.path.join(app.instance_path, 'development.yaml')
            app.config.from_file(config_file, load=yaml.safe_load)
    print(f"\napp.config['DATABASE_USER']: {app.config['DATABASE_USER']}\napp.config['DATABASE_ENGINE']: {app.config['DATABASE_ENGINE']}")

    from .product import product as product_blueprint
    app.register_blueprint(product_blueprint)

    from .model import db
    db.init_app(app)

    from . import model
    model.init_app(app)

    return app