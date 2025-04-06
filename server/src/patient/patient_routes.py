from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from src import mongo
from datetime import datetime
from bson.objectid import ObjectId

# Create a patient blueprint
patient_bp = Blueprint('patient', __name__)

# Function to check if user is a patient
def is_patient(email):
    user = mongo.db.users.find_one({"email": email})
    return user and user.get("role") == "patient"

# Function to check if user has access to a specific patient
def has_patient_access(user_email, patient_id):
    # Fetch user to get role
    user = mongo.db.users.find_one({"email": user_email})
    if not user:
        return False
    
    # Convert patient_id to ObjectId
    try:
        patient_obj_id = ObjectId(patient_id)
    except:
        return False
    
    # Find the patient record
    patient = mongo.db.patients.find_one({"_id": patient_obj_id})
    if not patient:
        return False
    
    # Check access rules:
    # 1. If user is a patient, they can only access their own record
    if user.get("role") == "patient":
        return str(user["_id"]) == patient.get("user_id")
    
    # 2. If user is a doctor or admin, they can access any patient
    if user.get("role") in ["doctor", "admin"]:
        return True
    
    return False

# Patient routes
# Get patient profile by ID
@patient_bp.route('/<patient_id>', methods=['GET'])
@jwt_required()
def get_patient(patient_id):
    # Get the current user's email from the JWT token
    current_user = get_jwt_identity()
    
    # Check access rights
    if not has_patient_access(current_user, patient_id):
        return jsonify({"error": "Unauthorized access"}), 403
    
    # Fetch patient record
    try:
        patient = mongo.db.patients.find_one({"_id": ObjectId(patient_id)})
    except:
        return jsonify({"error": "Invalid patient ID format"}), 400
    
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    
    # Convert ObjectId to string for JSON serialization
    patient["_id"] = str(patient["_id"])
    
    return jsonify({"patient": patient}), 200

# Update patient profile
@patient_bp.route('/update/<patient_id>', methods=['PUT'])
@jwt_required()
def update_patient(patient_id):
    # Get the current user's email from the JWT token
    current_user = get_jwt_identity()

    # Check access rights
    if not has_patient_access(current_user, patient_id):
        return jsonify({"error": "Unauthorized access"}), 403
    
    # Get request data
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    # Create update data dictionary
    update_data = {}
    allowed_fields = ["full_name", "date_of_birth", "id_number", "gender", "address", "phone"]
    for field in allowed_fields:
        if field in data:
            update_data[field] = data[field]

    update_data["updated_at"] = datetime.now()

    # Update patient record
    try:
        result = mongo.db.patients.update_one(
            {"_id": ObjectId(patient_id)},
            {"$set": update_data}
        )
    except:
        return jsonify({"error": "Invalid patient ID format"}), 400
    
    if result.matched_count == 0:
        return jsonify({"error": "Patient not found"}), 404
    
    return jsonify({"message": "Patient profile updated successfully"}), 200