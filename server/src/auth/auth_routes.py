from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from src import mongo
from src.auth.auth_middleware import create_access_token
from .user_model import UserModel, UserRole

# Create an auth blueprint
auth_bp = Blueprint('auth', __name__)

# Auth routes
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')
    role = data.get('role', UserRole.PATIENT.value)

    # Basic validation
    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400
    
    # Check if the user already exists
    existing_user = mongo.db.users.find_one({"email": email})
    if existing_user:
        return jsonify({"error": "User already exists"}), 400
    
    # Hash the password
    hashed_password = generate_password_hash(password)

    # Create a new user instance (no name field)
    new_user = UserModel(email=email, password=hashed_password, role=role)
    
    # Convert to dictionary for database storage
    user_dict = new_user.to_dict()
    
    # Insert user into the database
    result = mongo.db.users.insert_one(user_dict)
    user_id = result.inserted_id
    
    # If user is a patient, create an empty patient record
    if role == UserRole.PATIENT.value:
        # Create a minimal patient record linked to the user
        # Only include user_id and email
        patient_record = {
            "user_id": str(user_id),
            "email": email,
            "created_at": new_user.created_at,
            "updated_at": new_user.updated_at
        }
        
        # Insert the basic patient record
        mongo.db.patients.insert_one(patient_record)

    return jsonify({
        "message": "User created successfully",
        "user_id": str(user_id)
    }), 201

@auth_bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')
    
    # Basic validation
    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400
    
    # Check if the user exists
    user = mongo.db.users.find_one({"email": email})
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    # Check user password
    if not check_password_hash(user['password'], password):
        return jsonify({"error": "Invalid password"}), 401
    
    # Generate JWT token if email and password are valid
    token = create_access_token(identity=user['email'])
    
    # Return token in the response body with role info but without name
    return jsonify({
        "message": "Login successful",
        "token": token,
        "user": {
            "email": user['email'],
            "role": user.get('role', UserRole.PATIENT.value)
        }
    }), 200