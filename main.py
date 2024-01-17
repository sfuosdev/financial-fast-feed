from flask import Flask, jsonify

import os
from dotenv import load_dotenv
from flask_cors import CORS

from db import get_database

load_dotenv()
app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})  # This allows all origins for all routes

@app.route('/get-articles', methods=['GET'])
def get_articles():
    db = get_database(os.getenv('MONGODB_URI'), 'newsData')
    main_collection = db['Main']

    # Fetch the latest articles; here we assume the latest articles are inserted last
    articles_cursor = main_collection.find().limit(22)  # Adjust limit as needed
    articles = list(articles_cursor)

    # Convert ObjectId to string because ObjectId is not JSON serializable
    for article in articles:
        article['_id'] = str(article['_id'])

    return jsonify(articles)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)  # Heroku provides the port via env variable

