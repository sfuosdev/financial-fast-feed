"""
import feedparser

def parse_rss(url):
    feed = feedparser.parse(url)
    news_items = []

    for entry in feed.entries:
        news_item = {
            'title': entry.title,
            'pubDate': entry.published,
            'description': entry.summary,
            'link': entry.link  # URL to the full article
        }
        news_items.append(news_item)

    return news_items
"""
import ssl
import feedparser

def parse_rss(rss_url):
    # Create an SSL unverified context
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context

    # Parse the RSS feed
    feed = feedparser.parse(rss_url)

    news_items = []

    for entry in feed.entries:
        news_item = {
            'title': entry.title,
            'link': entry.link,
            'published': entry.published,
            'description': entry.description
        }
        news_items.append(news_item)

    return news_items

