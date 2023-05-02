import parse
from bs4 import BeautifulSoup
import os
import argparse
import re

# can try to print emails seperaterly
def p_links(url):
    anon = parse.browser_handle(url)
    try:
        print('\n[+] Printing Links and emails From BeautifulSoup.')
        soup = BeautifulSoup(anon, 'html.parser')
        links = [link.get('href') for link in soup.find_all('a', href=True)]
        print(*links, sep='\n')
    except Exception as e:
        print(f'{"":>3}[-] Exception: {e.__class__.__name__}')
        pass
    



url = 'https://www.3i-infotech.com'
p_links(url)

