#!/usr/bin/env python3

import requests
import re
from urllib.parse import urljoin
import argparse

def get_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target URL.")
    parser.add_argument("-w", "--wordlist", dest="wordlist", help="Full path to the wordlist to use.")
    parser.add_argument("-s", default=False, action="store_true", help="The site uses HTTPS rather than simple HTTP.")
    options = parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify target domain, use -h or --help for more info.")
    if not options.wordlist:
        parser.error("[-] Please specify a wordlist, use -h or --help for more info.")
    return options

options = get_argument()

def request(url, s):
    if s:
        url = "https://" + url
    else:
        url = "http://" + url
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

def extract_links(response):
    href_links = re.findall('(?:href=")(.*?)"', response)
    return href_links
try:
    with open(options.wordlist,"r") as wordlist_file:
        for line in wordlist_file:
            test_url = options.target
            word = line.strip()
            test_url = word+"." + options.target
            response = request(test_url, options.s)
            if response:
                print("\n\n\n\n------------------------LINKS FOR "+ test_url +"--------------------------")
                links_result = extract_links(str(response.content))
                unique_links = []
                for link in links_result:
                    link = urljoin(test_url, link)

                    if '#' in link:
                        link = link.split('#')[0]

                    if link not in unique_links and options.target in link:
                        print(link+"\n")
                        unique_links.append(link)
except KeyboardInterrupt:
	print("\n[+] Stopping the Crawler")
