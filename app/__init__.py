"""
This contains the application factory for creating flask application instances.
Using the application factory allows for the creation of flask applications configured 
for different environments based on the value of the CONFIG_TYPE environment variable
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_mail import Mail
from app.config import  os


### Flask extension objects instantiation ###
app = Flask(__name__)
ma = Marshmallow(app)
mail = Mail()
db = SQLAlchemy()

### Application Factory ###
def create_app():

    # Configure the flask app instance
    CONFIG_TYPE = os.getenv('CONFIG_TYPE')
    app.config.from_object(CONFIG_TYPE)

    # Register blueprints
    register_blueprints(app)

    # Initialize flask extension objects
    initialize_extensions(app)

    # Configure logging
    configure_logging(app)

    # Register error handlers
    register_error_handlers(app)

    return app


### Helper Functions ###
def register_blueprints(app):
    from app.blogs import blog

    app.register_blueprint(blog, url_prefix='/blog')

def initialize_extensions(app):
    mail.init_app(app)

    # Initialize db and create tables
    db.init_app(app)
    with app.app_context():
        db.create_all()

def register_error_handlers(app):
    pass


def configure_logging(app):
    pass