from datetime import datetime
from enum import Enum

# Define user role
class UserRole(Enum):
    PATIENT = "patient"
    DOCTOR = "doctor"
    ADMIN = "admin"

# Define user model
class UserModel:
    def __init__(self, email, password, role=UserRole.PATIENT.value, name=None):
        # Initialize user attributes
        self.email = email
        self.password = password
        self.role = role
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        # Convert user attributes to dictionary for database storage
        user_dict = {
            "email": self.email,
            "password": self.password,
            "role": self.role,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
        
        # Only include name if it's provided
        if self.name:
            user_dict["name"] = self.name
            
        return user_dict
    
    @classmethod
    def from_dict(cls, data):
        # Create a user instance from a dictionary for database retrieval
        user = cls(
            email=data.get("email"),
            password=data.get("password"),
            role=data.get("role", UserRole.PATIENT.value),
            name=data.get("name")
        )
        
        # Set timestamps if they exist in data
        if "created_at" in data:
            user.created_at = data["created_at"]
        if "updated_at" in data:
            user.updated_at = data["updated_at"]
            
        return user