from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from src import mongo
from datetime import datetime
from bson.objectid import ObjectId

# Create a doctor blueprint
doctor_bp = Blueprint('doctor', __name__)

# Function to check if user is a doctor
def is_doctor(email):
    user = mongo.db.users.find_one({"email": email})
    return user and user.get("role") == "doctor"

# Function to check if user has access to a specific doctor
def has_doctor_access(user_email, doctor_id):
    # Fetch user to get role
    user = mongo.db.users.find_one({"email": user_email})
    if not user:
        return False
    
    # Convert doctor_id to ObjectId
    try:
        doctor_obj_id = ObjectId(doctor_id)
    except:
        return False
    
    # Find the doctor record
    doctor = mongo.db.doctors.find_one({"_id": doctor_obj_id})
    if not doctor:
        return False
    
    # Check access rules:
    # 1. If user is a doctor, they can only access their own record
    if user.get("role") == "doctor":
        return str(user["_id"]) == doctor.get("user_id")
    
    # 2. If user is an admin, they can access any doctor
    if user.get("role") == "admin":
        return True
    
    return False

# Doctor routes
# Get doctor profile by ID
@doctor_bp.route('/<doctor_id>', methods=['GET'])
@jwt_required()
def get_doctor(doctor_id):
    # Get the current user's email from the JWT token
    current_user = get_jwt_identity()

    # Check access rights
    if not has_doctor_access(current_user, doctor_id):
        return jsonify({"error": "Unauthorized access"}), 403
    
    # Fetch doctor record
    try:
        doctor = mongo.db.doctors.find_one({"_id": ObjectId(doctor_id)})
    except:
        return jsonify({"error": "Invalid doctor ID format"}), 400
    
    if not doctor:
        return jsonify({"error": "Doctor not found"}), 404
    
    # Convert ObjectId to string for JSON serialization
    doctor["_id"] = str(doctor["_id"])
    
    return jsonify({"doctor": doctor}), 200

# Update doctor profile
@doctor_bp.route('/update/<doctor_id>', methods=['PUT'])
@jwt_required()
def update_doctor(doctor_id):
    # Get the current user's email from the JWT token
    current_user = get_jwt_identity()

    # Check access rights
    if not has_doctor_access(current_user, doctor_id):
        return jsonify({"error": "Unauthorized access"}), 403
    
    # Get request data
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    # Create update data dictionary
    update_data = {}
    allowed_fields = [
        "full_name", "license_number", "specialty", "education", 
        "biography", "years_of_experience", "profile_image",
        "contact_number", "office_address", "office_hours",
        "accepting_new_patients"
    ]
    
    for field in allowed_fields:
        if field in data:
            update_data[field] = data[field]

    update_data["updated_at"] = datetime.now()

    # Update doctor record
    try:
        result = mongo.db.doctors.update_one(
            {"_id": ObjectId(doctor_id)},
            {"$set": update_data}
        )
    except:
        return jsonify({"error": "Invalid doctor ID format"}), 400
    
    if result.matched_count == 0:
        return jsonify({"error": "Doctor not found"}), 404
    
    return jsonify({"message": "Doctor profile updated successfully"}), 200

# Doctor Dashboard
@doctor_bp.route('/dashboard', methods=['GET'])
@jwt_required()
def get_dashboard():
    # Get the current user's email from the JWT token
    current_user_email = get_jwt_identity()

    # Get user info
    user = mongo.db.users.find_one({"email": current_user_email})
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Check if user is a doctor
    if user.get("role") != "doctor":
        return jsonify({"error": "Only doctors can access this dashboard"}), 403

    # Find doctor record associated with this user
    doctor = mongo.db.doctors.find_one({"email": current_user_email})
    if not doctor:
        return jsonify({"error": "Doctor profile not found"}), 404

    # Convert ObjectId to string for JSON serialization
    doctor["_id"] = str(doctor["_id"])

    # Prepare dashboard data
    dashboard_data = {
        "doctor": doctor,
        "user": {
            "email": user["email"],
            "name": user.get("name"),
            "role": user.get("role")
        }
    }

    return jsonify(dashboard_data), 200

# Get doctors by specialty
@doctor_bp.route('/specialty/<specialty>', methods=['GET'])
def get_doctors_by_specialty(specialty):
    try:
        doctors = list(mongo.db.doctors.find({"specialty": specialty, "accepting_new_patients": True}))
        # Convert ObjectId to string for each doctor
        for doctor in doctors:
            doctor["_id"] = str(doctor["_id"])
        
        return jsonify({"doctors": doctors}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get all available doctors
@doctor_bp.route('/available', methods=['GET'])
def get_available_doctors():
    try:
        doctors = list(mongo.db.doctors.find({"accepting_new_patients": True}))
        # Convert ObjectId to string for each doctor
        for doctor in doctors:
            doctor["_id"] = str(doctor["_id"])
        
        return jsonify({"doctors": doctors}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500