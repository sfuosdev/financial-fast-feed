import logging
from openai import OpenAI
import os
import json
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import ssl
import feedparser
from rss.fetchRSS import fetch_full_article
from summarize import summarize_article
from db import get_database, insert_article
import requests
from bs4 import BeautifulSoup
from datetime import datetime

load_dotenv('.env')

app = Flask(__name__, static_folder="my-financial-news-app/build")
CORS(app)

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

@app.route('/articles', methods=['GET'])
def get_articles_api():
    db_uri = os.getenv('MONGODB_URI')
    db_name = 'newsData'
    client = MongoClient(db_uri, tlsAllowInvalidCertificates=True)
    db = client[db_name]
    articles_collection = db['Main']

    # Sort by '_id' in descending order to get the most recently inserted documents
    articles = list(articles_collection.find({}, {'_id': False}).sort("_id", -1).limit(32))
    print("Fetched articles from MongoDB:", articles)

    return jsonify(articles)


def fetch_full_article(article_url, max_paragraphs=3):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }
    try:
        response = requests.get(article_url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        article_body = soup.find_all(['p', 'h1', 'h2', 'h3'])

        truncated_article = ' '.join([para.get_text() for para in article_body[:max_paragraphs]])
        return truncated_article
    except Exception as e:
        return f"Error fetching full article: {e}"


def get_multiple_articles(rss_url, number_of_articles=2):
    articles_to_return = []
    feed = feedparser.parse(rss_url)

    print(f"Fetching RSS feed from: {rss_url}")
    if not feed.entries:
        print(f"No articles found in RSS feed: {rss_url}")
        return articles_to_return

    articles = feed.entries[:number_of_articles]

    for item in articles:
        try:
            full_article = fetch_full_article(item.link)
            summary = summarize_article(full_article)

            # Use the published date or current time if not available
            publication_date = item.get("published", datetime.utcnow().isoformat())

            article_data = {
                "title": item.get("title", "No title available"),
                "link": item.get("link", "No link available"),
                "description": item.get("description", "No description available"),
                "date": publication_date,
                "author": item.get("author", "No author available"),
                "summary": summary
            }
            articles_to_return.append(article_data)
        except Exception as e:
            print(f"Error processing article: {item.get('title', 'No title')} - {e}")

    return articles_to_return

def main():
    db = get_database(os.getenv('MONGODB_URI'), 'newsData')
    main_collection = db['Main']
    rss_urls = [
        # Crypto
        'https://Blockchain.News/RSS/',
        'https://bitcoinist.com/feed/',
        'https://www.newsbtc.com/feed/',
        'https://cointelegraph.com/rss',

        # Stock Market Movements
        'https://www.reutersagency.com/feed/?best-topics=business-finance&post_type=best',
        'https://seekingalpha.com/feed.xml',
        'https://fortune.com/feed/fortune-feeds/?id=3230629',

        # Economic Indicators
        'https://tradingeconomics.com/canada/rss',
        'https://tradingeconomics.com/united-states/rss',
    ]

    for rss_url in rss_urls:
        articles = get_multiple_articles(rss_url)
        if articles:
            for article in articles:
                insert_result = insert_article(main_collection, article)
                if insert_result:
                    print(f"Inserted article with ID: {insert_result.inserted_id}")
                else:
                    print("Failed to insert article.")
        else:
            print(f"No articles fetched from {rss_url}")

if __name__ == "__main__":
    main()  
