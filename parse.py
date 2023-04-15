import mechanize
import requests
import http.cookiejar
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# def user_agent_spoof(url):
#     browser = mechanize.Browser()
#     browser.set_handle_robots(False)
#     browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
#     page = browser.open(url)
#     source_code = page.read()
#     # x= browser.response().read()
#     # header = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1'



# def proxy(url):
#     proxies = {"https": "http://61.162.225.180:9091/" , 'http' : "http://61.162.225.180:9091/" }
#     r=requests.get( url2, proxies=proxies)
#     print(r.text)


# def cookie_meth(url): #visiting the webpage everytime with new cookie ID
#     browser = mechanize.Browser()
#     browser.set_handle_robots(False)
#     browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')] 
#     cookie_jar =http.cookiejar.LWPCookieJar()
#     browser.set_cookiejar(cookie_jar)
#     page = browser.open(url)
#     for i in cookie_jar:
#         print(i)

def browser_handle(url):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    # proxies = {"https": "http://61.111.38.5:80/" , 'http' : "http://61.111.38.5:80/" }
    # r=requests.get( url, proxies=proxies , verify=False)
    cookie_jar =http.cookiejar.LWPCookieJar()
    browser.set_cookiejar(cookie_jar)
    page = browser.open(url)
    source_code = page.read()
    for i in cookie_jar:
        print("New cookie" + str(i))
    # print(source_code)
    return source_code

if __name__ == '__main__':
    url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/" # agent string 
    url2 ="http://httpbin.org/ip" # IP
    url3 = 'https://www.kittenwar.com/'
    # user_agent_spoof(url)
    # proxy(url2)
    # cookie_meth(url3)
    #broser_handle(url)
