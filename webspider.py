#Partially Finished Code
'''
General Notes / Info Gathering:
This lab will use requests.get. The format for this is requests.get(url). For example:
    page = requests.get("http://mywebsite.com")
    print (page.text)

Goals:
1. Start with some base URL
2. Scan the HTML document and gather all the links <a href=””>.
3. Follow each of the new links and repeat.
4. Keep track of the links already visited (so as not to get caught in a loop).
'''

'''
How to start:
Break down into steps (you know more than you think).
Start simple, then build it out...  Add more as you get things working.
Get/Read/open a given URL
Start with a hard-coded variable
Look at the requests.get module
Get it to work and just print out what is received
Parse the returned string of data to extract URLs.
Look at the source - what does a URL/link look like? 
match with a regular expression 
Look at the re python module... 
Loop through to print out all URLs found...
Put discovered URLs into a list
Simple list object...
Pull each URL and parse for more URLs
Keep a list of URLs already visited
Check against the list before following any URL
'''
import requests as real_requests
from bs4 import BeautifulSoup

base_url = input("URL to Scan: ")
base_url = ___url__ = base_url

links_from_url = []
enum_links = []
url_visited = []
links_to_crawl = []

def scan_url(url):
    raw_url = []
    response = real_requests.get(url)
    text = BeautifulSoup(response.text, 'html.parser')
    links = text.find_all('a')
    for link in links:
        if link['href']:
            url = link['href']
            raw_url.append(url)
        elif not link['href']:
            pass
    return raw_url

def filter_url(url):
    filter_links = []
    for item in scan_url(url):
        if item.startswith("http"):
            filter_links.append(item)
            links_from_url.append(item)
            links_to_crawl.append(item)
        elif item.startswith("www"):
            filter_links.append(item)
            links_from_url.append(item)
            links_to_crawl.append(item)
    return filter_links

scan_url(base_url)
filter_url(base_url)
print(links_to_crawl)


def enum_website():
    url_visited.append(scan_url(base_url))
    for url in links_to_crawl:
        scan_url(url)
        filter_url(url)
        url_visited.append(url)
        if url.startswith("http"):
            enum_links.append(url)
        elif url.startswith("www"):
            enum_links.append(url)
    print(enum_links)



enum_website()