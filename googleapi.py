import requests
from googlesearch import search
import parse
from bs4 import BeautifulSoup

results =[]
query = " baba elaichi "
for x in search(query , num_results=20):
    results.append(x)
print(results)

info = []
for url in results:
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.title.string
        description = soup.find('meta', attrs={'name': 'description'})['content']
        info.append({'url': url, 'title': title, 'description': description})
    except:
        continue

# Print the useful information
print("Useful Information:")
for item in info:
    print(f"URL: {item['url']}")
    print(f"Title: {item['title']}")
    print(f"Description: {item['description']}")
    print("------------------------")

# searchr("Seed labs")