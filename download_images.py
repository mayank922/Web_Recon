import requests
from bs4 import BeautifulSoup
import re
import os

def download_image(img_url, folder_path):
    # get the image name from the url
    img_name = re.findall(r'/([\w_-]+[.](jpg|jpeg|img|png))$', img_url)
    try:
        img_data = requests.get(img_url).content
        with open(os.path.join(folder_path, img_name[0][0]), 'wb') as handler:
            handler.write(img_data)
    except Exception as e:
        print(f"Error occurred while downloading {img_url}: {e}")

def parse_html(url, folder_path):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # find all images in the HTML
    images = soup.find_all('img')
    for img in images:
        img_url = img.get('src')
        download_image(img_url, folder_path)

def parse_css(url, folder_path):
    page = requests.get(url)
    content = page.content.decode('utf-8')
    # find all urls of images in the CSS
    image_urls = re.findall(r'url\((.*?)\)', content)
    for img_url in image_urls:
        download_image(img_url, folder_path)

def parse_js(url, folder_path):
    page = requests.get(url)
    content = page.content.decode('utf-8')
    # find all urls of images in the JavaScript
    image_urls = re.findall(r'src=[\'"]?([^\'" >]+)', content)
    for img_url in image_urls:
        download_image(img_url, folder_path)

def main(url, folder_path):
    # create folder to store downloaded images
    os.makedirs(folder_path, exist_ok=True)
    # parse the website based on its front-end language
    if url.endswith('.html') or url.endswith('.htm'):
        parse_html(url, folder_path)
    elif url.endswith('.css'):
        parse_css(url, folder_path)
    elif url.endswith('.js'):
        parse_js(url, folder_path)
    else:
        print(f"Unsupported file type for {url}")

if __name__ == '__main__':
    url = 'https://www.3i-infotech.com'
    folder_path = './images'
    main(url, folder_path)
