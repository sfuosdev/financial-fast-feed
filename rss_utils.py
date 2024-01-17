import requests
from bs4 import BeautifulSoup
import feedparser
from summarize import summarize_article  # Assuming you have a summarize_article function

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
    Fetch and summarize articles from a given RSS URL.
    Returns a list of article data.
    """
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
