#!/usr/bin/env python3

import argparse
from annonce import Annonce, to_csv
from query import insert_annonce, get_all_annonces, connectToDatabase, disconnectDatabase

#from query import ***
#from scrap import  scrap_annonce, scrap_search_page

# scrap_search_page(num_page)
# need function to test Annonce exist in bdd
# scrap_annonce(url)
# need function to insert Annonce in BDD

# need function to get all annonces from BDD

parser = argparse.ArgumentParser(description='Scrap and manage scrapped data')
cmd_subparser = parser.add_subparsers(title='command', dest='cmd')

scrap_parser = cmd_subparser.add_parser('scrap', help='')
csv_parser = cmd_subparser.add_parser('csv', help='')
csv_parser.add_argument('--file', help='filename', required=True)

args = parser.parse_args()


def scrap():
    insertAnnonce(annonce)
    pass

def db_to_csv(filename):
    cnx = connectToDatabase()
    to_csv(filename, get_all_annonces(cnx))
    disconnectDatabase(cnx)
    print(filename)


if args.cmd == 'scrap':
    scrap()

elif args.cmd == 'csv':
    db_to_csv(args.file)

