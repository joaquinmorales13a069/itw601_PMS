from datetime import datetime
from enum import Enum
from bson.objectid import ObjectId
from src import mongo

class Specialty(Enum):
    GENERAL_MEDICINE = "General Medicine"
    CARDIOLOGY = "Cardiology"
    DERMATOLOGY = "Dermatology"
    NEUROLOGY = "Neurology"
    ORTHOPEDICS = "Orthopedics"
    PEDIATRICS = "Pediatrics"
    PSYCHIATRY = "Psychiatry"
    GYNECOLOGY = "Gynecology"
    OPHTHALMOLOGY = "Ophthalmology"
    ONCOLOGY = "Oncology"
    OTHER = "Other"

class Doctor:
    def __init__(self, user_id, email, full_name=None, license_number=None,
                 specialty=None, education=None, biography=None, 
                 years_of_experience=None, profile_image=None, contact_number=None, 
                 office_address=None, office_hours=None, accepting_new_patients=True):
        # Required fields linked to user account
        self.user_id = user_id
        self.email = email
        
        # Professional information
        self.full_name = full_name
        self.license_number = license_number
        self.specialty = specialty  # Can be from Specialty enum
        self.education = education  # List of educational backgrounds
        self.biography = biography  # Short professional bio
        self.years_of_experience = years_of_experience
        self.profile_image = profile_image  # URL or path to image
        
        # Contact and location information
        self.contact_number = contact_number
        self.office_address = office_address
        
        # Availability information
        self.office_hours = office_hours or {}  # Dictionary with days and hours
        self.accepting_new_patients = accepting_new_patients
        
        # Timestamps
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        # Convert Doctor object to dictionary for database storage
        doctor_dict = {
            "user_id": self.user_id,
            "email": self.email,
            "accepting_new_patients": self.accepting_new_patients,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

        # Only include optional fields if they have values
        if self.full_name:
            doctor_dict["full_name"] = self.full_name
        if self.license_number:
            doctor_dict["license_number"] = self.license_number
        if self.specialty:
            doctor_dict["specialty"] = self.specialty
        if self.education:
            doctor_dict["education"] = self.education
        if self.biography:
            doctor_dict["biography"] = self.biography
        if self.years_of_experience:
            doctor_dict["years_of_experience"] = self.years_of_experience
        if self.profile_image:
            doctor_dict["profile_image"] = self.profile_image
        if self.contact_number:
            doctor_dict["contact_number"] = self.contact_number
        if self.office_address:
            doctor_dict["office_address"] = self.office_address
        if self.office_hours:
            doctor_dict["office_hours"] = self.office_hours

        return doctor_dict

    @classmethod
    def from_dict(cls, data):
        # Create a Doctor object from a dictionary for database retrieval
        doctor = cls(
            user_id=data.get("user_id"),
            email=data.get("email"),
            full_name=data.get("full_name"),
            license_number=data.get("license_number"),
            specialty=data.get("specialty"),
            education=data.get("education"),
            biography=data.get("biography"),
            years_of_experience=data.get("years_of_experience"),
            profile_image=data.get("profile_image"),
            contact_number=data.get("contact_number"),
            office_address=data.get("office_address"),
            office_hours=data.get("office_hours"),
            accepting_new_patients=data.get("accepting_new_patients", True)
        )

        # Set timestamps if they exist in data
        if "created_at" in data:
            doctor.created_at = data["created_at"]
        if "updated_at" in data:
            doctor.updated_at = data["updated_at"]

        return doctor
    
    @staticmethod
    def get_doctor_by_id(doctor_id):
        """Get a doctor by their ID"""
        try:
            doctor_data = mongo.db.doctors.find_one({"_id": ObjectId(doctor_id)})
            if not doctor_data:
                return None
            # Convert ObjectId to string for JSON serialization
            doctor_data["_id"] = str(doctor_data["_id"])
            return doctor_data
        except Exception:
            return None
    
    @staticmethod
    def get_doctor_by_user_id(user_id):
        """Get a doctor by their user ID"""
        try:
            doctor_data = mongo.db.doctors.find_one({"user_id": user_id})
            if not doctor_data:
                return None
            # Convert ObjectId to string for JSON serialization
            doctor_data["_id"] = str(doctor_data["_id"])
            return doctor_data
        except Exception:
            return None
    
    @staticmethod
    def get_doctors_by_specialty(specialty):
        """Get all doctors by specialty"""
        try:
            doctors = list(mongo.db.doctors.find({"specialty": specialty}))
            # Convert ObjectId to string for each doctor
            for doctor in doctors:
                doctor["_id"] = str(doctor["_id"])
            return doctors
        except Exception:
            return []
    
    @staticmethod
    def get_available_doctors():
        """Get all doctors accepting new patients"""
        try:
            doctors = list(mongo.db.doctors.find({"accepting_new_patients": True}))
            # Convert ObjectId to string for each doctor
            for doctor in doctors:
                doctor["_id"] = str(doctor["_id"])
            return doctors
        except Exception:
            return []