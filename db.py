from pymongo import MongoClient

def connect_to_mongodb(uri):
    """
    Establishes a connection to MongoDB.
    """
    client = MongoClient(uri)
    return client

def insert_article(db, article_data):
    """
    Inserts a single article into the MongoDB database.
    """
    articles_collection = db.articles
    return articles_collection.insert_one(article_data)
