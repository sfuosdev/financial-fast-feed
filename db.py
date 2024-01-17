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

def insert_article(db, article_data):
    try:
        articles_collection = db.articles
        insert_result = articles_collection.insert_one(article_data)
        logging.info(f"Article inserted with id: {insert_result.inserted_id}")
        return insert_result
    except Exception as e:
        logging.error(f"Error inserting article: {e}")
        return None
