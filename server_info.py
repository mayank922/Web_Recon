import builtwith
import requests

def serverinfo(target_website):
    result = builtwith.builtwith("https://www." + target_website)
    #options=["font-scripts","tag-managers" ,"photo-galleries" , "javascript-frameworks" ,"widgets","web-frameworks","cms","programming-languages","blogs","marketing-automation"]
    x= " , ".join(result["web-frameworks"])
    
    y =" ".join(result["programming-languages"])
    print("Programming language used by the webpage -->" + y)
    print("Web frameworks used by the webpage --> " + x)

    response = requests.get("https://www." + target_website)
    print("Server used by the webpage --> " + response.headers["server"])


# import urllib.request, json 
# target_website = "192.168.116.134"
#bw = BuiltWith("c65ba0f5-298b-4c68-8abf-76cc33a57b2c")

# response = requests.get("https://api.builtwith.com/free1/api.json?KEY=c65ba0f5-298b-4c68-8abf-76cc33a57b2c&LOOKUP=hackthissite.org")
# #print(respones.json())
# if response.status_code == 200:
#     # Print the technology tags for the website
#     for tag in response.json()["Results"][0]["Result"]["Tags"]:
#         print(tag["Name"])
# else:
#     print("Failed to retrieve data from BuiltWith API")


# with urllib.request.urlopen("https://api.builtwith.com/free1/api.json?KEY=c65ba0f5-298b-4c68-8abf-76cc33a57b2c&LOOKUP=vulnweb.com") as url:
#     data = json.load(url)
#     print(data)