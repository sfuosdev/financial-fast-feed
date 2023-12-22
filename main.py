from rss.parseRSS import parse_rss
from rss.fetchRSS import fetch_full_article
import requests 
import feedparser

def fetch_and_parse_rss(url):
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
    response = requests.get(url, headers=headers)
    feed = feedparser.parse(response.content)
    return feed.entries

def get_full_articles(rss_url):
    news_items = fetch_and_parse_rss(rss_url)
    
    for entry in news_items:
        print(f"Title: {entry.title}")
        print(f"Date: {entry.published}")
        print(f"Description: {entry.summary}")
        # Assuming fetch_full_article is implemented to fetch the full text
        full_text = fetch_full_article(entry.link) if 'link' in entry else None
        print(f"Full Text: {full_text}\n\n")

# Example usage
if __name__ == "__main__":
    rss_url = 'https://tradingeconomics.com/united-states/rss'
    get_full_articles(rss_url)