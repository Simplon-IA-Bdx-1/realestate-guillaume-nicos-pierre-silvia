#!/usr/bin/env python3

import argparse
from annonce import Annonce, to_csv
from query import insert_annonce, get_all_annonces, connectToDatabase, disconnectDatabase
from scrap import scrap_annonce, scrap_search_page, scrap_annonce_text
from time import sleep
import glob, os

#from query import ***
#from scrap import  scrap_annonce, scrap_search_page

# scrap_search_page(num_page)
# need function to test Annonce exist in bdd
# scrap_annonce(url)
# need function to insert Annonce in BDD

# need function to get all annonces from BDD

parser = argparse.ArgumentParser(description='Scrap and manage scrapped data')
cmd_subparser = parser.add_subparsers(title='command', dest='cmd', required=True)

scrap_parser = cmd_subparser.add_parser('scrap', help='scrap the first search page')
scrap_parser.add_argument('--dir', help='scrap a directory containing html files')
csv_parser = cmd_subparser.add_parser('csv', help='download the database as a csv file')
csv_parser.add_argument('--file', help='filename', required=True)

args = parser.parse_args()

# This function is the main one : launch all the scraping process.
def scrap():
    """Launch the process to scrap the page of a special ad"""
    cnx = connectToDatabase()
    if args.dir is None:
        urls =  scrap_search_page(1)
        sleep(5)
        print(urls)
        for url in urls:
            annonce = scrap_annonce(url)
            sleep(5)
            print(annonce)
            if annonce is not None:
                insert_annonce(cnx,annonce)
    else:
        for filename in glob.glob(args.dir + "/*.html"):
            print(filename)
            with open(filename, errors="ignore") as file:
                annonce = scrap_annonce_text(file.read())
                

                if annonce is not None:
                    #print(annonce)
                    insert_annonce(cnx,annonce)
    disconnectDatabase(cnx)
        
# Creates a csv with all ads requested.
def db_to_csv(filename):
    """Creates a csv with all ads requested."""
    cnx = connectToDatabase()
    to_csv(filename, get_all_annonces(cnx))
    disconnectDatabase(cnx)
    print(filename)


if args.cmd == 'scrap':
    scrap()

elif args.cmd == 'csv':
    db_to_csv(args.file)

