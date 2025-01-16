from pymongo import MongoClient
import logging

# Function to connect to MongoDB
def connect_to_mongodb(uri):
    try:
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
        result = collection.insert_one(article)
        print(f"Article inserted with ID: {result.inserted_id}")
        return result
    except Exception as e:
        print(f"Failed to insert article into MongoDB: {e}")
        return None

