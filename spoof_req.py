import mechanize
import requests
import http.cookiejar
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def browser_handle(url):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    cookie_jar =http.cookiejar.LWPCookieJar()
    browser.set_cookiejar(cookie_jar)
    page = browser.open(url, timeout=5)
    source_code = page.read()
    # for i in cookie_jar:
    #     print("New cookie" + str(i))
    # print(source_code)
    return source_code

if __name__ == '__main__':
    url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/" # agent string 
    url2 ="http://httpbin.org/ip" # IP
    url3 = 'https://www.kittenwar.com/'
    # user_agent_spoof(url)
    # proxy(url2)
    # cookie_meth(url3)
    #browser_handle(url)
