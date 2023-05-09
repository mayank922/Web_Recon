import argparse
import parse_links
import extract_email
import openports
import googleapi
import images_downloader
from art import *

if __name__ == "__main__":
    tprint("Web-Con",font="3d_diognal")
    parser = argparse.ArgumentParser(description="Will be edited")
    parser.add_argument("-l" ,required=False, dest="links", help="specify the domain")
    parser.add_argument("-e" ,required=False, dest="emails" ,help="specify the domain" )
    parser.add_argument("-p" ,required=False, dest="port" ,help="specify the domain")
    parser.add_argument("-g" ,required=False, dest="gsearch" ,help="specify the query of choice")
    parser.add_argument("-i" ,required=False, dest="img" ,help="specify the domain")
    parser.add_argument("-a" ,required=False, dest="all_out" ,help="specify the domain")
    

    args = parser.parse_args()
    links = args.links
    emails=args.emails
    port = args.port
    gsearch = args.gsearch
    img = args.img
    all_out = args.all_out
    if links:
        parse_links.p_links(links)
    
    if emails:
        extract_email.extract_email(emails)
    
    if port:
        openports.scan_port(port)
    
    if gsearch:
        googleapi.query_search(gsearch)
    

    if img:
        images_downloader.main(img)

    if all_out:
        openports.scan_port(port)
        print("------------------------")
        parse_links.p_links(links)
        print("------------------------")
        extract_email.extract_email(emails)
        print("------------------------")
        googleapi.query_search(gsearch)
        print("------------------------")
        images_downloader.main(img)
        print("------------------------")