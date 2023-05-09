import builtwith
import requests

target_website = "192.168.116.134"

def serverinfo(target_website):
    result = builtwith.builtwith("https://www." + target_website)
    #options=["font-scripts","tag-managers" ,"photo-galleries" , "javascript-frameworks" ,"widgets","web-frameworks","cms","programming-languages","blogs","marketing-automation"]
    x= " , ".join(result["web-frameworks"])
    y =" ".join(result["programming-languages"])
    print("Programming language used by the webpage -->" + y)
    print("Web frameworks used by the webpage --> " + x)

    response = requests.get("https://www." + target_website)
    print("Server used by the webpage --> " + response.headers["server"])


serverinfo(target_website)