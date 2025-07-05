import requests
from bs4 import BeautifulSoup

urls = ["https://www.bbc.com/sport", "https://www.foxsports.com/", "http://www.espn.in","https://edition.cnn.com/sport"]

def get_sports_headlines(urls):
    headers = {'User-Agent': 'Mozilla/5.0'}
    headlines = []

    for url in urls:
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()  # Check for HTTP errors
            soup = BeautifulSoup(response.text, 'html.parser')

            for tag in soup.find_all(['h1', 'h2', 'h3']):
                text = tag.get_text(strip=True)
                if text and len(text) > 10:
                    headlines.append(text)
        except Exception as e:
            print(f"Failed to fetch from {url}: {e}")

    return headlines

# Get headlines
headlines = get_sports_headlines(urls)

# Save to file
with open("sports_headlines.txt", "a", encoding="utf-8") as f:
    for line in headlines:
        f.write(line + "\n")
