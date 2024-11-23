import trafilatura 

# Function to fetch and extract the main content of an article from a URL
def fetch_full_article(url):
    downloaded = trafilatura.fetch_url(url)
    text = trafilatura.extract(downloaded)
    return text