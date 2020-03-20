# SCRAPPING

## **Structure**

* .env = contains accesses to the database
* [announce.py](https://github.com/Simplon-IA-Bdx-1/realestate-guillaume-nicos-pierre-silvia/blob/master/scrapper/annonce.py) = Announcement class containing the constructor and all the methods related to this class
* [query.py](https://github.com/Simplon-IA-Bdx-1/realestate-guillaume-nicos-pierre-silvia/blob/master/scrapper/query.py) = contains all queries to the database
* [scrap.py](https://github.com/Simplon-IA-Bdx-1/realestate-guillaume-nicos-pierre-silvia/blob/master/scrapper/scrap.py) = contains scrapping methods
* [scrapper.py](https://github.com/Simplon-IA-Bdx-1/realestate-guillaume-nicos-pierre-silvia/blob/master/scrapper/scrapper.py) = allows local scrapping (see command lines below)
* [selenium.py](https://github.com/Simplon-IA-Bdx-1/realestate-guillaume-nicos-pierre-silvia/blob/master/scrapper/selenium.py) / [selenium.ipynb](https://github.com/Simplon-IA-Bdx-1/realestate-guillaume-nicos-pierre-silvia/blob/dev/scrapper/selenium.ipynb) = online scrapping of all ads

>More precision => What is selenium? <br />
>**Definition :** Selenium is a Python library allowing to imitate the behavior of a normal user who consults real estate ads in our case
><p align="center"><img width=65% src="https://zupimages.net/up/20/12/eieu.png"></p>

## **Usage**

### By command lines

- If you want to scrap the first page of housings to rent at Bordeaux on Seloger.com
```bash
./scrapper.py scrap
```
- If you want to scrap the ads on a directory. Each page will be downloaded into a html file : *ad_id*.html
```bash
./scrapper.py scrap --dir <dirname>
```

- If you want to create a CSV file from the database
```bash
./scrapper.py csv --file <csvfile>
```


## **Support**

If you need help, please enter this command line in order to generate a Pydoc for the script you need help about :
```bash
python -m pydoc <filename.py>
```
