#!/usr/bin/python
# -*- coding: utf-8 -*-

from annonce import Annonce
import requests
from bs4 import BeautifulSoup
import json

#import re


# Function which returns a json of keys and values on an ad's webpage.
def scrap_annonce_text(content):
    """Returns a json with all information for a special ad."""
    soup = BeautifulSoup(content, "html.parser")
    # infobox = soup.find(id="showcase-description")
    
    # data = {}
    
    # sections = infobox.contents
    # # text sections[1]
    # regex = re.compile('.*TitledDescription.*')
    # desc_all = sections[1].find("div", {"class": regex})
    # data['description'] = desc_all.find("p").text
    
    # # Général section[2]
    # general = sections[2].find("h3", text="Général").nextSibling.ul
    # for item in general.contents:
    #     if "surface" in item.text.lower():
    #         regex = re.compile('(\d+)(?=m²)')
    #         match = re.search(regex, item.text)
    #         if match:
    #             data['surface'] = match.group(1)
    #         else:
    #             print(item.text)
    #     elif "pièces" in item.text.lower():
    #         regex = re.compile('(\d+)')
    #         match = re.search(regex, item.text)
    #         if match:
    #             data['nb_pieces'] = match.group(1)
    #         else:
    #             print(item.text)
    #     elif "chambre" in item.text.lower():
    #         regex = re.compile('(\d+)')
    #         match = re.search(regex, item.text)
    #         if match:
    #             data['nb_chambres'] = match.group(1)
    #         else:
    #             print(item.text)
    #     elif "étage" in item.text.lower():
    #         regex = re.compile('(\d+)')
    #         match = re.search(regex, item.text)
    #         if match:
    #             data['etage'] = match.group(1)
    #         else:
    #             print(item.text)

    # interieur = sections[2].find("h3", text="A l'intérieur").nextSibling.ul
    # data['si_sdEau'] = 0
    # data['si_sdbain'] = 0
    # for item in interieur.contents:
    #     if "salle d'eau" in item.text.lower():
    #         data['si_sdEau'] = 1           
    #     elif "salle de bain" in item.text.lower():
    #         data['si_sdbain'] = 1
    #     elif "Chauffage" in item.text:
    #         regex = re.compile('(?:Chauffage )(.*)')
    #         match = re.search(regex, item.text)
    #         if match:
    #             data['idtypechauffage'] = match.group(1)
    #         else:
    #             print(item.text)
    #     elif "Cuisine" in item.text:
    #         regex = re.compile('(?:Cuisine )(.*)')
    #         match = re.search(regex, item.text)
    #         if match:
    #             data['idtypechauffage'] = match.group(1)
    #         else:
    #             print(item.text)
    # regex = re.compile(".*PreviewFocusedTile")
    # energy = sections[3].find("div", {"class": regex})
    # if energy is not None:
    #     data['dpeL'] = energy.p.text
    #     data['dpeC'] = int(energy.span.text)

    # price = sections[4].div.div.div.text
    # regex = re.compile('(\d*)')
    # match = re.search(regex, price)
    # data['prix'] = match.group(0)

    # print(data)
    
    # print(info_section.contents)
    
    scripts = soup.find_all("script")
    json_data = None
    for script in scripts:
        if len(script.contents) > 0 :
            lines = script.contents[0].splitlines()
            #if len(lines) > 1:
            if "window[\"initialData\"]" in lines[0]:
                data = lines[0]
                data = data.lstrip("window[\"initialData\"] = JSON.parse(")
                data = data.rstrip("\");")
                data = data.replace("\\u0022", "\"")
                # data = data.replace("\\u00e9", "é")
                # data = data.replace("\\u00b2", "²")
                # data = data.replace(r"\u00e8", "è")
                #data = data.replace("\\/", "\\")
                
                
                #                 data = script.contents[0]
                #                 data = data[data.find("products : ["):data.find("//")].strip("products : [")
                try:
                    json_data = json.loads(data)
                    # print(json.dumps(json_data, indent=2))
                except:
                    print(data)
                    return None
    data_dict = {}   
    if json_data is not None:
        for key, value in list(json_data['meta'].items()):
            if key in Annonce.fields:
                data_dict[key] = json_data['meta'][key]
        for key, value in list(json_data['tracking']['infos'].items()):
            if key in Annonce.fields:
                data_dict[key] = json_data['tracking']['infos'][key]
                
        if 'idTypeCuisine' in json_data['meta'].keys():
            data_dict['idtypecuisine'] = json_data['meta']['idTypeCuisine']
        if 'idTypeChauffage' in json_data['meta'].keys():
            data_dict['idtypechauffage'] = json_data['meta']['idTypeChauffage']
            # print(data_dict['idtypechauffage'])

        data_dict['ville'] = json_data['advert']['mainAdvert']['address']['city']

        # json_data['advert']['mainAdvert']['adress']['neighbourhood']
        # json_data['advert']['mainAdvert']['plusFeatures']
        
        for feature_set in json_data['advert']['mainAdvert']['generalFeatures']:
            for feature in feature_set['list']:
                feature = feature['text']
                # print(feature)
                if "Chauffage" in feature:
                    data_dict['idtypechauffage'] = feature.lstrip("Chauffage ")
                
                if "Cuisine" in feature:
                    data_dict['idtypecuisine'] = feature.lstrip("Cuisine ")

        data_dict['description'] = json_data['advert']['mainAdvert']['description']

        for key in Annonce.fields:
            if key not in data_dict.keys():
                print("missing key: ", key)
 
    print(data_dict)
    return Annonce(**data_dict)

# The function needs you to give an URL.
def scrap_annonce(url):
    """Scrap a page of a property"""
    page = requests.get(url)
    content = page.text
    return scrap_annonce_text(content)

# The function is waiting for a page number to scrap
# Example : for page 6, "num_page" = 6
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
