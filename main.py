from rss.fetchRSS import fetch_full_article
from summarize import summarize_article

from db import connect_to_mongodb, insert_article

from bs4 import BeautifulSoup
import requests 
import feedparser

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

def get_multiple_articles(rss_url, number_of_articles=2):
    """
    Fetches multiple articles from an RSS feed.
    number_of_articles: Number of articles to process from the feed.
    """
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
    response = requests.get(rss_url, headers=headers)

    if response.status_code == 200:
        feed = feedparser.parse(response.content)
        articles = feed.entries[:number_of_articles]  # Process the specified number of articles

        for item in articles:
            title = item.get('title', 'No title available')
            link = item.get('link', 'No link available')
            description = item.get('description', 'No description available')
            pub_date = item.get('published', 'No publication date available')
            author = item.get('author', 'No author available')

            full_article = fetch_full_article(link)
            summary = summarize_article(full_article)

            print(f"Title: {title}\nLink: {link}\nDescription: {description}\nDate: {pub_date}\nAuthor: {author}\nSummary: {summary}\n")
    else:
        print(f"Failed to fetch RSS feed. HTTP Status Code: {response.status_code}")

if __name__ == "__main__":
    mongodb_uri = "URI"
    db_client = connect_to_mongodb(mongodb_uri)
    db = db_client.newsData.Main # Replace with your database name
    # RSS Feeds looped through, fetched, and summarized
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

    # Process articles from each feed
    for rss_url in rss_urls:
        print(f"Fetching articles from: {rss_url}\n")
        articles = get_multiple_articles(rss_url)
        
        for article in articles:
            # Prepare the article data for insertion
            article_data = {
                "title": article["title"],
                "link": article["link"],
                "description": article["description"],
                "date": article["pub_date"],
                "author": article["author"],
                "summary": article["summary"]
            }

            # Insert the article data into MongoDB
            insert_article(db, article_data)
        
        print("\n-----\n")