import ssl
import feedparser

# Function to parse RSS feed from a given URL
def parse_rss(rss_url):
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context

    print(f"Fetching RSS feed from: {rss_url}")
    
    feed = feedparser.parse(rss_url)

    if feed.bozo:
        print(f"Error parsing RSS feed from {rss_url}: {feed.bozo_exception}")
        return []

    if not feed.entries:
        print(f"No entries found in RSS feed: {rss_url}")
        return []

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
