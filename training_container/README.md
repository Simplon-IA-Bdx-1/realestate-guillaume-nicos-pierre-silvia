# Training Container

## Project Structure

```
|__ Dockerfile 
|__ Model.py
|__ init.sh
|__ requirements.txt
|__ training.cron
|__ README.md 
```

## Project details

* [training.cron](https://github.com/Simplon-IA-Bdx-1/realestate-guillaume-nicos-pierre-silvia/blob/dev/training_container/training.cron) : use of **Cron** format to define time and frequency of our web scrapping (every friday at 6 pm CET Paris)

* [Model.py](https://github.com/Simplon-IA-Bdx-1/realestate-guillaume-nicos-pierre-silvia/blob/dev/training_container/Model.py) : define the complete pipeline for scrapping, create csv file with all important informations, create the real-estate-model.pkl and the insertion of all informations into the two databases (Annonces and Models)