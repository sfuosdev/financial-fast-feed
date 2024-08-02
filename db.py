from pymongo import MongoClient
import logging
import os

def connect_to_mongodb(uri):
    try:
        client = MongoClient(uri)
        client.admin.command('ping')
        logging.info("Successfully connected to MongoDB!")
        return client
    except Exception as e:
        logging.error(f"Failed to connect to MongoDB: {e}")
        return None

def get_database(uri, dbname):
    client = connect_to_mongodb(uri)
    if client is not None:
        return client[dbname]
    else:
        logging.error("Client is None, cannot get database.")
        return None

def insert_article(collection, article):
    try:
        insert_result = collection.insert_one(article)
        print(f"Inserted article with ID: {insert_result.inserted_id}")
        return insert_result
    except Exception as e:
        print(f"Error inserting article: {e}")
        return None
