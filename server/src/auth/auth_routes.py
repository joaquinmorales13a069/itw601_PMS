from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from src import mongo
from .user_model import User

# Create an auth blueprint
auth_bp = Blueprint('auth', __name__)


# Auth routes
@auth_bp.route('/login')
def login():
    """Login endpoint."""
    return "Login"

@auth_bp.route('/register', methods=['POST'])
def register():
    """Register endpoint: create new user """
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    """Basic validation"""
    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400
    
    """Check if user already exists"""
    existing_user = mongo.db.users.find_one({"email": email})
    if existing_user:
        return jsonify({"error": "User already exists"}), 400
    
    """Hash the password"""
    hashed_password = generate_password_hash(password)

    """Create a User object"""
    new_user = User(email=email, password=hashed_password)

    """Insert the user into the database"""
    mongo.db.users.insert_one({
        "email": new_user.email,
        "password": new_user.password
    })

    return jsonify({"message": "User created successfully"}), 201