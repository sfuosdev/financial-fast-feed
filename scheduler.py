import os
import time
import logging
from rss_utils import get_multiple_articles
from db import get_database, insert_article

FETCH_INTERVAL = 600 # TEMP TIMING (8 Hour Intervals Main)

def fetch_and_store_articles():
    db = get_database(os.getenv('MONGODB_URI'), 'newsData')
    if db is None:
        logging.error("Failed to connect to the database.")
        return
    
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
                logging.info(f"Inserted article with ID: {insert_result.inserted_id}")
            else:
                logging.error("Failed to insert article.")

def schedule_fetch():
    while True:
        try:
            fetch_and_store_articles()
            time.sleep(FETCH_INTERVAL)
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            # Decide if you want to stop or wait after an error
            break  # or use time.sleep(ERROR_INTERVAL) for a delay before retrying

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    schedule_fetch()
