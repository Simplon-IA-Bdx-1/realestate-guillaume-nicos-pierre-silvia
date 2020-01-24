# SCRAPPING

## **Utilisation**

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

### By our API

*To be completed*

<br />

## **Support**

If you need help, please enter this command line in order to generate a Pydoc for the script you need help about :
```bash
python -m pydoc <filename.py>
```
