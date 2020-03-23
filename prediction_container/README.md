# API with Flask

## Project Structure

```
|__ Dockerfile 
|__ README.md 
|__ requirements.txt
|__ www
    |__ app.py
    |__ templates
        |__ formulaire.html
        |__ resultats.html
```
<br/>

## Project details

* JSON request (GET and POST) [app.py](https://github.com/Simplon-IA-Bdx-1/realestate-guillaume-nicos-pierre-silvia/blob/dev/prediction_container/www/app.py)

* html pages [templates](https://github.com/Simplon-IA-Bdx-1/realestate-guillaume-nicos-pierre-silvia/tree/dev/prediction_container/www/templates)

<br/>

## Curl examples

To see a specific add :
```
curl --request GET 'http://localhost:8081/api' \
--header 'Content-Type: application/json' \
--data-raw '{
    "typedebien" : "Appartement",
    "codepostal" : "33000",
    "surface" : "100",
    "nb_pieces" : "5",
    "idtypechauffage" : "électrique",
    "idtypecuisine" : "aucune",
    "si_balcon" : 0,
    "nb_chambres" : 3,
    "si_sdbain" : 1,
    "si_sdEau" : 1,
    "etage" : 3,
    "dpeC" : 70
}'
```
To see which model is currently been used :
```
curl 'http://localhost:8081/model/current'
```

To see the list of models :
```
curl 'http://localhost:8081/model/list'
```
To set a specific model as the the model currently been used :
```
curl 'http://localhost:8081/model/set' -d  "model_name=realestate-model-2020-23-03-10h41m-rmsle-0.195.pkl"
```
<br/>

## Navigate to http://localhost:8081

## Site **SelogerML**:

<p align="center"><img src="https://zupimages.net/up/20/12/omsq.png"></p>
