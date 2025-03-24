from flask import Flask
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv
import sys

# Initialize Flask app
app = Flask(__name__)

# Load environment variables from the .env file
load_dotenv()
mongo_uri = os.getenv("MONGO_URI")

# Check if MONGO_URI is available
if not mongo_uri:
    print("ERROR: MONGO_URI environment variable not found. Check your .env file.")
    sys.exit(1)

app.config["MONGO_URI"] = mongo_uri

try:
    mongo = PyMongo(app)
    # Test the connection
    mongo.db.list_collection_names()
    print("Successfully connected to MongoDB")
except Exception as e:
    print(f"ERROR connecting to MongoDB: {e}")
    sys.exit(1)

@app.route('/')
def home():
    # Example: fetching collection names
    collections = mongo.db.list_collection_names()
    return f"Collections in database: {collections}"

if __name__ == '__main__':
    app.run(debug=True)