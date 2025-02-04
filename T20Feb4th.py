#Task 20: Use the requests and BeautifulSoup libraries to scrape the titles of articles from a website (e.g., a news website).
import requests
from bs4 import BeautifulSoup

def get_article_titles(url):
    try:
        # Send a GET request to the website
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all article titles (modify the tag/class based on the website structure)
        titles = [title.get_text(strip=True) for title in soup.find_all('h2')]
        
        return titles if titles else ["No articles found"]
    
    except requests.exceptions.RequestException as e:
        return [f"Error: {e}"]

# Example usage
url = "https://timesofindia.indiatimes.com/defaultinterstitial.cms?b=/"  
url = "https://timesofindia.indiatimes.com/india/language-of-urban-naxals-politics-of-poison-pm-modis-all-out-attack-against-rahul-gandhi-in-lok-sabha/articleshow/117920331.cms"
article_titles = get_article_titles(url)

# Print the article titles
for idx, title in enumerate(article_titles, start=1):
    print(f"{idx}. {title}")
