from src import create_app, mongo

app = create_app()

@app.route('/db-status')
def db_status():
    try:
        # Check if we can access the MongoDB server
        mongo.db.command('ping')
        return {
            "status": "connected", 
            "database": mongo.db.name,
            "message": "Successfully connected to MongoDB"
        }
    except Exception as e:
        return {
            "status": "error", 
            "message": f"Database connection error: {str(e)}"
        }, 500

if __name__ == '__main__':
    try:
        print(f"Connecting to database: {mongo.db.name}")
        # Test the connection
        mongo.db.command('ping')
        print(f"Successfully connected to MongoDB database: {mongo.db.name}")
    except Exception as e:
        print(f"Database connection error: {str(e)}")
    
    app.run(debug=True)