from rss.fetchRSS import fetch_full_article
from summarize import summarize_article


from bs4 import BeautifulSoup
import requests 
import feedparser

def fetch_full_article(article_url, max_paragraphs=5):
    """
    Fetches and truncates the full article content from a given URL.
    max_paragraphs: Maximum number of paragraphs to include in the summary.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
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

def get_one_article(rss_url):
    """
    Fetches one article from an RSS feed.
    """
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
    response = requests.get(rss_url, headers=headers)

    if response.status_code == 200:
        feed = feedparser.parse(response.content)
        if feed.entries:
            item = feed.entries[0]  # Get the first article
            title = item.get('title', 'No title available')
            link = item.get('link', 'No link available')
            description = item.get('description', 'No description available')
            pub_date = item.get('published', 'No publication date available')
            author = item.get('author', 'No author available')

            full_article = fetch_full_article(link)
            summary = summarize_article(full_article)

            print(f"Title: {title}\nLink: {link}\nDescription: {description}\nDate: {pub_date}\nAuthor: {author}\nSummary: {summary}")
        else:
            print("No items found in the RSS feed.")
    else:
        print(f"Failed to fetch RSS feed. HTTP Status Code: {response.status_code}")

if __name__ == "__main__":
    # Example RSS URL
    rss_url = 'link'

    # Process the article from the feed
    get_one_article(rss_url)

