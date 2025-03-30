from datetime import datetime
from enum import Enum
from bson.objectid import ObjectId
from src import mongo

class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"

class Patient:
    def __init__(self, user_id, email, full_name=None, date_of_birth=None, 
                 id_number=None, gender=None, address=None, phone=None):
        # Required fields
        self.user_id = user_id
        self.email = email
        
        # Optional fields that will be set through CRUD operations
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.id_number = id_number
        self.gender = gender
        self.address = address
        self.phone = phone
        
        # Timestamps
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def to_dict(self):
        # Convert Patient object to dictionary for database storage
        patient_dict = {
            "user_id": self.user_id,
            "email": self.email,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
        
        # Only include optional fields if they have values
        if self.full_name:
            patient_dict["full_name"] = self.full_name
        if self.date_of_birth:
            patient_dict["date_of_birth"] = self.date_of_birth
        if self.id_number:
            patient_dict["id_number"] = self.id_number
        if self.gender:
            patient_dict["gender"] = self.gender
        if self.address:
            patient_dict["address"] = self.address
        if self.phone:
            patient_dict["phone"] = self.phone
            
        return patient_dict
    
    @classmethod
    def from_dict(cls, data):
        # Create a Patient object from a dictionary for database retrieval
        patient = cls(
            user_id=data.get("user_id"),
            email=data.get("email"),
            full_name=data.get("full_name"),
            date_of_birth=data.get("date_of_birth"),
            id_number=data.get("id_number"),
            gender=data.get("gender"),
            address=data.get("address"),
            phone=data.get("phone")
        )
        
        # Set timestamps if they exist in data
        if "created_at" in data:
            patient.created_at = data["created_at"]
        if "updated_at" in data:
            patient.updated_at = data["updated_at"]
            
        return patient