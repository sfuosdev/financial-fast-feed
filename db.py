from pymongo import MongoClient
import logging

def connect_to_mongodb(uri):
    try:
        client = MongoClient(uri)
        return client
    except Exception as e:
        logging.error(f"Failed to connect to MongoDB: {e}")
        return None

def get_database(uri, dbname):
    client = connect_to_mongodb(uri)
    if client is not None:
        return client[dbname]
    else:
        return None

def insert_article(db, article_data):
    try:
        articles_collection = db.articles
        return articles_collection.insert_one(article_data)
    except Exception as e:
        print(f"Error inserting article: {e}")
        return None

