import socket
import nmap
from nmap import PortScanner


# Define target website
# target_website = "192.168.116.134"



def scan_port(target_website):
    open_ports = []
    # Get IP address of the website
    ip_address = socket.gethostbyname(target_website)
    print("IP address:", ip_address)

    # Get domain name from IP address
    domain_name = socket.getfqdn(ip_address)
    print("Domain name:", domain_name)

    # Create an nmap scanner object
    nm = nmap.PortScanner()

    # Scan for open ports on the website
    try:
        nm.scan(target_website, arguments='-p 1-1000, -sV')
        for port in nm[target_website]['tcp']:
            if nm[target_website]['tcp'][port]['state'] == 'open':
                print("Port:", port) 
                print("Service:", nm[target_website]['tcp'][port]['name'])
                print("Version:", nm[target_website]['tcp'][port]['version'])
                print("--------------------")

    except:
        nm.scan(ip_address, arguments='-p 1-1000, -sV')

        for port in nm[ip_address]['tcp']:
            if nm[ip_address]['tcp'][port]['state'] == 'open':
                print("Port:", port) 
                print("Service:", nm[ip_address]['tcp'][port]['name'])
                print("Version:", nm[ip_address]['tcp'][port]['version'])
                print("--------------------")
    #print(nm.scan)

    # Print out the list of open ports
    
    
    
    

    
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
