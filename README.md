<p align="center"><img width=45% src="https://zupimages.net/up/20/03/0tej.png"></p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Python](https://img.shields.io/badge/python-v3.7-blue.svg)
![Jupyter Notebook](https://img.shields.io/badge/Jupyter%20Notebooks-yes-red)
![Docker](https://img.shields.io/badge/docker-yes-green.svg)
<a href="https://github.com/Simplon-IA-Bdx-1/realestate-guillaume-nicos-pierre-silvia/commits/master"><img src="https://img.shields.io/github/last-commit/Simplon-IA-Bdx-1/realestate-guillaume-nicos-pierre-silvia/master"/></a>


<br/>

# :one: Project's objectives

What we have been asked to do is a complete scrapping pipeline of rental property advertisements in Bordeaux surroundings to insert this information into a database.
At the same time, a machine learning model will be established and will make predictions based on certain parameters filled in from a dedicated web interface.

**Chosen website:** SeLoger.com


# :two: Content of the project

## **Structure**

|      |  Folder to see for more details
|     :---:    |      :---:      |
| &nbsp;&nbsp;Database | [Here](https://github.com/Simplon-IA-Bdx-1/realestate-guillaume-nicos-pierre-silvia/blob/master/BDD/README.md) |
| &nbsp;&nbsp;Notebooks | [Here](https://github.com/Simplon-IA-Bdx-1/realestate-guillaume-nicos-pierre-silvia/blob/master/notebooks/README.md) |
| &nbsp;&nbsp;Prediction_container | [Here](https://github.com/Simplon-IA-Bdx-1/realestate-guillaume-nicos-pierre-silvia/blob/master/prediction_container/README.md) |
| &nbsp;&nbsp;Scrapping | [Here](https://github.com/Simplon-IA-Bdx-1/realestate-guillaume-nicos-pierre-silvia/blob/master/scrapper/README.md) |
| &nbsp;&nbsp;Selenium_scrapper_container | [Here](https://github.com/Simplon-IA-Bdx-1/realestate-guillaume-nicos-pierre-silvia/blob/master/selenium_scrapper_container/README.md) |
| &nbsp;&nbsp;Training_container | [Here](https://github.com/Simplon-IA-Bdx-1/realestate-guillaume-nicos-pierre-silvia/blob/master/training_container/README.md) |

<br/>

## **Packages required and version** 

If the version isn't mentioned, it is the latest.<br/>


|         Module        |        Version        |
|          :---:        |         :---:         |
|mysql-connector-python |                       |
|numpy                  |                       |
|selenium               |                       |
|requests               |                       |
|pandas                 |        0.24.2         |
|seaborn                |                       |
|matplotlib             |        3.1.2          |
|beautifulsoup4         |                       |
|xgboost                |          0.80         |

<br />

All modules are included into the [requirements.txt](https://github.com/Simplon-IA-Bdx-1/realestate-guillaume-nicos-pierre-silvia/blob/master/requirements.txt)

## **Installation**

```bash
pip install -r requirements.txt
```

## :three: **Command lines**

## :four: **Create and start containers**

```bash
docker-compose build trainer
```
and then

```bash
docker-compose up
```

You'll see the logs :

<p align="center"><img src="https://zupimages.net/up/20/12/zens.png"></p>

Scraping will be operated every sunday at 6:00 pm

If you try to connect to http://localhost:8081, you will see :

<p align="center"><img src="https://zupimages.net/up/20/12/omsq.png"></p>

# Authors

If you like our work :

**Guillaume** : [GitHub](https://github.com/guitoo)<br/>
**Nicolas** : [GitHub](https://github.com/nicolasseverino)<br/>
**Pierre** : [GitHub](https://github.com/pierremirandebroucas)<br/>
**Silvia** : [GitHub](https://github.com/Beatrix84)

<br/>

<p align="center"><img width=35% src="https://zupimages.net/up/20/04/62bu.jpg"></p>