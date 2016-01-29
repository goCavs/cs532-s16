from bs4 import BeautifulSoup, SoupStrainer
import requests
import sys

url = sys.argv[1]

r = requests.get(url)
data = r.text
for link in BeautifulSoup(data, "html.parser", parse_only=SoupStrainer('a')):
    if link.has_attr('href'):
        response = requests.get(link['href'])
        if response.headers['Content-Type'] == 'application/pdf':
            #this one is a pdf
            print response.url, response.headers['Content-Length']
