from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os
from src.config import config
from src.auth.auth_middleware import init_jwt

# Initialize extensions
mongo = PyMongo()

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
    
    # Register routes
    from src.routes import register_routes
    register_routes(app)
    
    return app