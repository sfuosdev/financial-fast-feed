from pymongo import MongoClient
import logging
from dotenv import load_dotenv
load_dotenv()
import os


MONGO_URI = os.getenv("MONGODB_URI")
# Function to connect to MongoDB
def connect_to_mongodb(uri):
    try:
        print(f"🔍 Trying to connect to MongoDB: {MONGO_URI}")  # Debugging line
        client = MongoClient(uri)
        client.admin.command('ping')
        logging.info("Successfully connected to MongoDB!")
        return client
    except Exception as e:
        logging.error(f"Failed to connect to MongoDB: {e}")
        return None

# Function to retrieve a specific database by name
def get_database(uri, dbname):
    client = connect_to_mongodb(uri)
    if client is not None:
        return client[dbname]
    else:
        logging.error("Client is None, cannot get database.")
        return None

# Function to insert an article document into a collection
def insert_article(collection, article):
    try:
        insert_result = collection.insert_one(article)
        print(f"Inserted article with ID: {insert_result.inserted_id}")
        return insert_result
    except Exception as e:
        print(f"Error inserting article: {e}")
        return None
