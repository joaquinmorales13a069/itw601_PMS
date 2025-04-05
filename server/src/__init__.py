from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os
from src.config import config
from src.auth.auth_middleware import init_jwt

# Initialize extensions
mongo = PyMongo()

def init_db(app):
    """Initialize database collections and indexes."""
    with app.app_context():
        # Create unique index on email for users collection
        mongo.db.users.create_index("email", unique=True)
        # Create index on user_id for patients collection
        mongo.db.patients.create_index("user_id")
        # Create index on email for patients collection
        mongo.db.patients.create_index("email")

def create_app(config_name='default'):
    # Create Flask application
    app = Flask(__name__)
    
    # Load environment variables
    load_dotenv()
    
    # Load configuration
    app.config.from_object(config[config_name])
    
    # Initialize MongoDB with the app
    mongo.init_app(app)

    # Initialize JWT manager
    init_jwt(app)
    
    # Initialize database indexes
    init_db(app)
    
    # Register routes
    from src.routes import register_routes
    register_routes(app)
    
    return app