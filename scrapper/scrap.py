#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

with open("test.html", "r") as f:    
    contents = f.read()
    soup = BeautifulSoup(contents, 'html.parser')
    print(soup.prettify())