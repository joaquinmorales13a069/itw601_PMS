from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from datetime import timedelta

jwt = JWTManager()

def init_jwt(app):
    """Initialize JWT manager with app."""

    # JWT Configuration
    app.config['JWT_SECRET_KEY'] = app.config['SECRET_KEY']
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)
    app.config['JWT_TOKEN_LOCATION'] = ['headers']

    # Initialize JWT with app
    jwt.init_app(app)

    # JWT error handling
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        """Callback for expired tokens."""
        return {
            'status': 401,
            'message': 'Token has expired'
        }, 401
    
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        """Callback for invalid tokens."""
        return {
            'status': 401,
            'message': 'Invalid token'
        }, 401