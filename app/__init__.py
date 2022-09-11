from flask import Flask
from flask_migrate import Migrate
from config import configs
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs[config])
    db = SQLAlchemy(app)
    from app.main import main
    app.register_blueprint(main)
    return app




