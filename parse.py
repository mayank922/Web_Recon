import mechanize
import requests

def user_agent_spoof(url):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    page = browser.open(url)
    source_code = page.read()
    x= browser.response().read()
    header = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1'
    for item in x:
        if item == header:
            print(item)
            break
    else:
        print("no there")



def proxy(url):
    proxies = {"https": "http://61.162.225.180:9091/" , 'http' : "http://61.162.225.180:9091/" }
    r=requests.get( url2, proxies=proxies)
    print(r.text)

if __name__ == '__main__':
    url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/" # agent string 
    url2 ="http://httpbin.org/ip" # IP
    user_agent_spoof(url)
    proxy(url2)

