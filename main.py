from rss.parseRSS import parse_rss
from rss.fetchRSS import fetch_full_article
import requests 
import feedparser
from bs4 import BeautifulSoup

def fetch_full_article(article_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }
    try:
        response = requests.get(article_url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Adjust the tags as per the website's structure
        article_body = soup.find_all(['p', 'h1', 'h2', 'h3'])
        full_text = ' '.join([para.get_text() for para in article_body])
        return full_text
    except Exception as e:
        return f"Error fetching full article: {e}"

def get_one_article(rss_url):
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
    response = requests.get(rss_url, headers=headers)

    if response.status_code == 200:
        feed = feedparser.parse(response.content)
        
        if feed.entries:
            item = feed.entries[1]  # Get the first article

            title = item.get('title', 'No title available')
            link = item.get('link', 'No link available')
            description = item.get('description', 'No description available')
            pub_date = item.get('published', 'No publication date available')
            author = item.get('author', 'No author available')

            full_article = fetch_full_article(link)

            print(f"Title: {title}\nLink: {link}\nDescription: {description}\nDate: {pub_date}\nAuthor: {author}\nFull Article: {full_article}")
        else:
            print("No items found in the RSS feed.")
    else:
        print(f"Failed to fetch RSS feed. HTTP Status Code: {response.status_code}")

# Example usage
if __name__ == "__main__":
    rss_url = 'https://cointelegraph.com/rss'
    get_one_article(rss_url)