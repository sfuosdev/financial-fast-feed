from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient
import jwt
import datetime
import os
from dotenv import load_dotenv
from db import get_database

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
    
# Initialize Blueprint
auth_bp = Blueprint("auth", __name__)

# Get database connection
db = get_database(os.getenv('MONGODB_URI'), 'newsData')

users_collection = db["users"]

@auth_bp.route("/register", methods=["Post"])
def register():
    data = request.get_json()
    if not data or "email" not in data or "password" not in data or "username" not in data:
        return jsonify({"error":"Missing Required Fields"}),400
    
    if users_collection.find_one({"email":data["email"]}):
        return jsonify({"error":"Email already Registered"})

    hashed_password = generate_password_hash(data["password"])
    
    user_data = {
        "username": data["username"],
        "email": data["email"],
        "password": hashed_password,
        "created_at": datetime.datetime.utcnow()
    }
    users_collection.insert_one(user_data)
    
    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route("/login", methods=["Post"])

def login():
    data = request.get_json()
    
    if not data or "email" not in data or "password" not in data:
        return jsonify({"error": "Missing email or password"}), 400

    # Find user in database
    user = users_collection.find_one({"email": data["email"]})
    if not user:
        return jsonify({"error": "Invalid credentials"}), 401
    
    if not check_password_hash(user["password"], data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401
    
    


    token_payload = {
        "sub": user["email"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }
    
    token = jwt.encode(token_payload, SECRET_KEY, algorithm="HS256")
    return jsonify({"access_token": token, "username": user["username"]}), 200

# JWT Authentification 
# Anyone can access the API route, users need to send valid JWT token for routes

# Decorator
def token_required(f):
    # Accept any arguments the inital function accepts
    # Handles the token verificatino and calls route funcion if succesful
    def decorated_function(*args, **kwargs):
        token = request.headers.get("Authorization") # Extract your token
        if not token:
            return jsonify({"error": "Token is missing!"}), 401  # Unauthorized
        
        try:
            token = token.split(" ")[1]  # Remove 'Bearer ' prefix
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])  # Verify token
            user_email = decoded_token["sub"]  # Extract email from token payload
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token has expired!"}), 401  # Unauthorized
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token!"}), 401  # Unauthorized

        return f(user_email, *args, **kwargs)  # Pass the user email to the protected route

    decorated_function.__name__ = f.__name__
    return decorated_function


@auth_bp.route("/protected", methods=["GET"])
@token_required
def protected_route(user_email):
    return jsonify({"message": f"Access granted to {user_email}!"}), 200

    