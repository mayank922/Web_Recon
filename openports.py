import socket
import nmap
from nmap import PortScanner
import builtwith
import requests


# Define target website
# target_website = "192.168.116.134"



def scan_port(target_website):

    # Get IP address of the website
    ip_address = socket.gethostbyname(target_website)
    print("IP address:", ip_address)

    # Get domain name from IP address
    domain_name = socket.getfqdn(ip_address)
    print("Domain name:", domain_name)

    # Create an nmap scanner object
    nm = nmap.PortScanner()

    # Scan for open ports on the website
    nm.scan(target_website, arguments='-p 1-1000, -sV')
    #print(nm.scan)

    # Print out the list of open ports
    open_ports = []
    for port in nm[target_website]['tcp']:
        if nm[target_website]['tcp'][port]['state'] == 'open':
            print("Port:", port) 
            print("Service:", nm[target_website]['tcp'][port]['name'])
            print("Version:", nm[target_website]['tcp'][port]['version'])
            print("--------------------")
    
    

    result = builtwith.builtwith("https://www." + target_website)
    #options=["font-scripts","tag-managers" ,"photo-galleries" , "javascript-frameworks" ,"widgets","web-frameworks","cms","programming-languages","blogs","marketing-automation"]
    x= " , ".join(result["web-frameworks"])
    y =" ".join(result["programming-languages"])
    print("Programming language used by the webpage -->" + y)
    print("Web frameworks used by the webpage --> " + x)

    response = requests.get("https://www." + target_website)
    print("Server used by the webpage --> " + response.headers["server"])
    #         open_ports.append(port)
    # print("Open ports:", open_ports)



# scan_port(target_website)

# import socket
# import nmap
# from nmap import PortScanner


# # Define target website
# target_website = "192.168.116.137"


# # Get IP address of the website
# ip_address = socket.gethostbyname(target_website)
# print("IP address:", ip_address)

# # Get domain name from IP address
# domain_name = socket.getfqdn(ip_address)
# print("Domain name:", domain_name)

# # Create an nmap scanner object
# nm = nmap.PortScanner()

# # Scan for open ports on the website
# nm.scan(target_website, arguments='-p-, -sV')
# #print(nm.scan)

# # Print out the list of open ports
# open_ports = []
# for port in nm[target_website]['tcp']:
#     if nm[target_website]['tcp'][port]['state'] == 'open':
#         print("Port:", port) 
#         print("Service:", nm[target_website]['tcp'][port]['name'])
#         print("Version:", nm[target_website]['tcp'][port]['version'])
#         print("--------------------")