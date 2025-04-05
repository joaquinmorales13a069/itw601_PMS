import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')
    MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://itw601:itw601-password@panel.sosmedical.com.ni:27018/patient_management_system?authSource=admin&tls=false')

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    MONGO_URI = os.environ.get('TEST_MONGO_URI', 'mongodb://itw601:itw601-password@panel.sosmedical.com.ni:27018/test_patient_management?authSource=admin&tls=false')

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