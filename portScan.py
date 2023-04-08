import socket
import nmap


# Define target website
target_website = "192.168.116.137"

# Get IP address of the website
ip_address = socket.gethostbyname(target_website)
print("IP address:", ip_address)

# Get domain name from IP address
domain_name = socket.getfqdn(ip_address)
print("Domain name:", domain_name)

# Create an nmap scanner object
nm = nmap.PortScanner()

# Scan for open ports on the website
nm.scan(target_website, arguments='-p-')

# Print out the list of open ports
open_ports = []
for port in nm[target_website]['tcp']:
    if nm[target_website]['tcp'][port]['state'] == 'open':
        open_ports.append(port)
print("Open ports:", open_ports)