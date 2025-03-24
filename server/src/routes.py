from flask import Blueprint, jsonify

# Create a main blueprint
main_bp = Blueprint('main', __name__)

# Basic routes
@main_bp.route('/')
def index():
    """Root endpoint - API status."""
    return jsonify({
        "status": "online",
        "message": "API is running"
    })

@main_bp.route('/health')
def health_check():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "version": "1.0.0"
    })

def register_routes(app):
    """Register all blueprints/routes with the app."""
    app.register_blueprint(main_bp)
    
    # When you want to add more blueprints in the future, add them here
    # Example: app.register_blueprint(another_blueprint)