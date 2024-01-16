from rss.fetchRSS import fetch_full_article
from summarize import summarize_article

import os

from db import get_database, insert_article

from bs4 import BeautifulSoup
import requests 
import feedparser
from dotenv import load_dotenv

load_dotenv()

def fetch_full_article(article_url, max_paragraphs=3):
    """
    Fetches and truncates the full article content from a given URL.
    max_paragraphs: Maximum number of paragraphs to include in the summary.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }
    try:
        response = requests.get(article_url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        article_body = soup.find_all(['p', 'h1', 'h2', 'h3'])

        # Truncate the article to the specified number of paragraphs
        truncated_article = ' '.join([para.get_text() for para in article_body[:max_paragraphs]])
        return truncated_article
    except Exception as e:
        return f"Error fetching full article: {e}"

# Function to fetch and summarize articles from a given RSS URL
def get_multiple_articles(rss_url, number_of_articles=2):
    articles_to_return = []
    feed = feedparser.parse(rss_url)
    articles = feed.entries[:number_of_articles]

    for item in articles:
        full_article = fetch_full_article(item.link)
        summary = summarize_article(full_article)
        
        article_data = {
            "title": item.get("title", "No title available"),
            "link": item.get("link", "No link available"),
            "description": item.get("description", "No description available"),
            "date": item.get("published", "No publication date available"),
            "author": item.get("author", "No author available"),
            "summary": summary
        }
        articles_to_return.append(article_data)

    return articles_to_return

if __name__ == "__main__":
    # Retrieve the MongoDB URI from an environment variable
    mongodb_uri = os.getenv('MONGODB_URI')
    if not mongodb_uri:
        raise ValueError("No MONGODB_URI set for environment")

    db = get_database(mongodb_uri, 'newsData')

    if db is not None: 
        main_collection = db['Main']
        rss_urls = [
            #Crypto
            'https://Blockchain.News/RSS/',
            'https://bitcoinist.com/feed/',
            'https://www.newsbtc.com/feed/',
            # Stock Market Movements
            'https://www.reutersagency.com/feed/?best-topics=business-finance&post_type=best',
            'https://seekingalpha.com/feed.xml',
            'https://feeds.a.dj.com/rss/RSSMarketsMain.xml',
            'https://www.frbsf.org/our-district/about/sf-fed-blog-rss-feed/',
            # Economic Indicators
            'https://tradingeconomics.com/canada/rss',
            'https://tradingeconomics.com/united-states/rss',
            'https://feeds.content.dowjones.io/public/rss/mw_topstories',
            'https://api.io.canada.ca/io-server/gc/news/en/v2?dept=departmentfinance&type=newsreleases&sort=publishedDate&orderBy=desc&publishedDate%3E=2020-08-09&pick=100&format=atom&atomtitle=Canada%20News%20Centre%20-%20Department%20of%20Finance%20Canada%20-%20News%20Releases'
        ]

        for rss_url in rss_urls:
            articles = get_multiple_articles(rss_url)
            for article in articles:
                insert_result = insert_article(main_collection, article)
                if insert_result:
                    print(f"Inserted article with ID: {insert_result.inserted_id}")
                else:
                    print("Failed to insert article.")
