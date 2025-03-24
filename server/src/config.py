import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')
    MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/patient_management')

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    MONGO_URI = os.environ.get('TEST_MONGO_URI', 'mongodb://localhost:27017/test_patient_management')

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    TESTING = False

# Export configs
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}