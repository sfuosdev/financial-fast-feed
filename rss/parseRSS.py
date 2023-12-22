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
