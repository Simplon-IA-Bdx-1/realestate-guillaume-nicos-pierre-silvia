#!/usr/bin/python
# -*- coding: utf-8 -*-

from annonce import Annonce
import requests
from bs4 import BeautifulSoup
import json

def scrap_annonce(url):
    """Scrap a page of a property"""
    page = requests.get(url)
    content = page.text
    soup = BeautifulSoup(content, "html.parser")

    scripts = soup.find_all("script")
    json_data = None
    for script in scripts:
        if len(script.contents) > 0 :
            lines = script.contents[0].splitlines()
            if len(lines) > 1:
                if "var ava_data" in lines[1]:
                    data = script.contents[0]
                    data = data[data.find("products : ["):data.find("//")].strip("products : [")
                    json_data = json.loads(data)

    if json_data is not None:
        for key, value in list(json_data.items()):
            if key not in Annonce.fields:
                json_data.pop(key)
                #print(f"{key} : {value}")
        return Annonce(**json_data)
    return None
    

    annonce = Annonce(**{'idannonce':12345, 'prix':12345})
    return annonce



def scrap_search_page(num_page):  
    """Scrap the search page in order to find properties to scrap"""

    url = "https://www.seloger.com/list.htm?projects=2&types=1,2&natures=1,2,4&places=[{ci:330063}]&enterprise=0&qsVersion=1.0&LISTING-LISTpg="\
         + str(num_page)

    page = requests.get(url)
        
    soup = BeautifulSoup(page.text, 'html.parser')
    
    annonces = soup.find_all("a", attrs={"name": "classified-link"})
    urls = []

    for annonce in annonces:
        urls.append(annonce['href'])
    # print(urls)

    return urls


if __name__ == "__main__":

    url = "https://www.seloger.com/annonces/locations/appartement/paris-11eme-75/153697733.htm?projects=1&types=2,1&natures=1&places=[{div:2238}]&enterprise=0&qsVersion=1.0&bd=ListToDetail"
    annonce = scrap_annonce(url)
    print(annonce)
