import mechanize
url  = "https://www.bleepingcomputer.com/"

browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
page = browser.open(url)
source_code = page.read()
print(source_code)
