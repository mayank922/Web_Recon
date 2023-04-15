import parse
from bs4 import BeautifulSoup
import os
import argparse
import re


def p_links(url):
    anon = parse.browser_handle(url)
    try:
        print('[+] Printing Links From Regex.')
        link_finder = r'href="(.*?)"'
        links = re.findall(link_finder, anon)
        print(*links, sep='\n')
    except Exception as e:
        print(f'{"":>3}[-] Exception: {e.__class__.__name__}')
        pass

    try:
        print('\n[+] Printing Links From BeautifulSoup.')
        soup = BeautifulSoup(anon, 'html.parser')
        links = [link.get('href') for link in soup.find_all('a', href=True)]
        print(*links, sep='\n')
    except Exception as e:
        print(f'{"":>3}[-] Exception: {e.__class__.__name__}')
        pass
    



url = 'https://www.kittenwar.com/'
p_links(url)

