#!/usr/bin/python
# -*- coding: utf-8 -*-

from annonce import Annonce

from bs4 import BeautifulSoup

with open("test.html", "r") as f:    
    contents = f.read()
    soup = BeautifulSoup(contents, 'html.parser')
    print(soup.prettify())

    
def scrap_annonce(url):
    """Scrap a page of a property"""

    annonce = Annonce(**{'idannonce':12345, 'prix':12345})
    return annonce

def scrap_search_page(num_page):
    """Scrap the search page in order to find properties to scrap"""

    urls = []
    idannonces = []
    #for ****
    #    urls.append(url)
    return (urls,idannonces)
