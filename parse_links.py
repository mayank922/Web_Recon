import spoof_req
from bs4 import BeautifulSoup
import os
import argparse


def p_links(url):

    anon = spoof_req.browser_handle("https://www." +url) # respose returned from spoof_req.py
    try:
        print('\n[+] Printing Links')
        soup = BeautifulSoup(anon, 'html.parser')
        links = [link.get('href') for link in soup.find_all('a', href=True)]
        print(*links, sep='\n')
    except Exception as e:
        print(f'{"":>3}[-] Exception: {e.__class__.__name__}')
        pass
    



#url = 'https://www.3i-infotech.com'


