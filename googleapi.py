import requests
from googlesearch import search
import spoof_req
from bs4 import BeautifulSoup


results =[]
query = " 3i infotech"
for x in search(query , num_results=5):
    results.append(x)
print(results)

info = []
for url in results:
    try:
        response= spoof_req.browser_handle(url) #respose returned from spoof_req.py
        print(1)
        soup = BeautifulSoup(response, "html.parser")
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