import requests
import re
import spoof_req

def extract_email(domain):

    response = spoof_req.browser_handle('http://' + domain)

    # Extract email addresses listed on the website
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email_list = re.findall(email_regex, str(response))
    print('List of email addresses found on the website:')
    for email in email_list:
        print(email)

    # Extract email addresses commented/hidden in the code
    comment_regex = r'<!--.*?-->'
    code_comments = re.findall(comment_regex, str(response), re.DOTALL)
    for comment in code_comments:
        email_list += re.findall(email_regex, comment)
    print('List of email addresses found in the code comments:')
    for email in email_list:
        print(email)
