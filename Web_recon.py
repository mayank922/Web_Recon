import argparse
import parse_links
import extract_email
import portScan
import googleapi

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Wiil be edited")
    parser.add_argument("-l" ,required=False, dest="links", help="")
    parser.add_argument("-e" ,required=False, dest="emails" ,help="print the emails", action="store_true")
    parser.add_argument("-p" ,required=False, dest="port" ,help="prints the ports",action="store_true")
    parser.add_argument("-g" ,required=False, dest="gsearch" ,help="Search for usefull information on google",action="store_true")

    args = parser.parse_args()
    links = args.links
    emails=args.emails
    port = args.port
    gsearch = args.gsearch

    if links:
        