import requests
import re
import spoof_req

# Set the target IP address or domain name
target = 'www.3i-infotech.com'

# Send a GET request to the target website
response = requests.get('http://' + target)

# Extract email addresses listed on the website
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
email_list = re.findall(email_regex, response.text)
print('List of email addresses found on the website:')
for email in email_list:
    print(email)

# Extract email addresses commented/hidden in the code
comment_regex = r'<!--.*?-->'
code_comments = re.findall(comment_regex, response.text, re.DOTALL)
for comment in code_comments:
    email_list += re.findall(email_regex, comment)
print('List of email addresses found in the code comments:')
for email in email_list:
    print(email)
