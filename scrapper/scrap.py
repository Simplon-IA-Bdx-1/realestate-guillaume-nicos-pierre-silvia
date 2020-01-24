#!/usr/bin/python
# -*- coding: utf-8 -*-

from annonce import Annonce
import requests
from bs4 import BeautifulSoup
import json

def scrap_annonce_text(content):
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
                    try:
                        json_data = json.loads(data)
                    except:
                        print(data)
                        return None

    if json_data is not None:
        for key, value in list(json_data.items()):
            if key not in Annonce.fields:
                json_data.pop(key)
                #print(f"{key} : {value}")
        selected_description = []
        description_tag =  soup.findAll('section', class_='categorie')
        #diagnostic_tag = soup.find('section', class_='categorie u-padb')
        for theme in description_tag :
            #if theme != diagnostic_tag :
            #print(theme.get_text())
            selected_description.append(theme.get_text())
        if len(selected_description) > 1:
            selected_description.pop()
        
        json_data['description'] = "".join(selected_description)
        #for blabla in description_tag:
        print(selected_description)
        #print(diagnostic_tag)
        return Annonce(**json_data)

def scrap_annonce(url):
    """Scrap a page of a property"""
    page = requests.get(url)
    content = page.text
    return scrap_annonce_text(content)

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
