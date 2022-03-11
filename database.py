import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
from app import app


def get_source(url):
    """Return the source code for the provided URL. 

    Args: 
        url (string): URL of the page to scrape.

    Returns:
        response (object): HTTP response object from requests_html. 
    """

    try:
        session = HTMLSession()
        response = session.get(url)

        return response

    except requests.exceptions.RequestException as e:
        print(e)
def scrape_google(query):

    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.co.uk/search?q=" + query)
    
    links = list(response.html.absolute_links)
    google_domains = ('https://www.google.', 
                      'https://google.', 
                      'https://webcache.googleusercontent.', 
                      'http://webcache.googleusercontent.', 
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.')

    for url in links[:]:
        if url.startswith(google_domains):
            links.remove(url)

    return links

#results = scrape_google("How much RAM does valorant")
#print(results[1])

form_data = {'Memory': 'value1', 'Processor': 'value2'}
response = requests.post("https://store.steampowered.com/app/1245620/ELDEN_RING/", data=form_data)
print(response.text)
