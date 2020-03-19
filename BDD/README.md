# DATABASE ANNONCES

## List of appartments
[01-annonces.sql](https://github.com/Simplon-IA-Bdx-1/realestate-guillaume-nicos-pierre-silvia/blob/dev/BDD/init-db/01-annonces.sql)

## Structure

|   Fields  |  Description  |  Example |
|     :---:    |      :---:      |         :---:         |
|id <br/>(Primary key - Unique) | Id in the database. | 100 |<br/>
|idannonce <br/> | Identification number of the concerned good. | 155142519 |<br/>
|typedebien | Type of the housing. | Appartement |<br/>
|codepostal | Postal code of the city. | 75002 |<br/>
|codeinsee | Postal code & quarter identification. | 75102 |<br/>
|ville | Geographical location of the housing. | Paris |<br/>
|etage | At which stage is it located. | 3 |<br/>
|idtypechauffage | Characteristics of property heating (if heating). | Individuel électrique |<br/>
|idtypecuisine | Presence of a kitchen or not. | 0 if there isn't a kitchen / 1 if there is |<br/>
|si_balcon | Presence of a balcony or not. | 0 if there isn't a balcony / 1 if there is |<br/>
|nb_chambres | How many bedrooms in the housing. | 2 |<br/>
|nb_pieces | How many rooms in the housing. | 2 |<br/>
|si_sdbain | Presence of a bath or not. | 0 if there isn't a bath / 1 if there is |<br/>
|si_sdEau | Presence of a shower or not. | 0 if there isn't at least one shower / 1 if there is |<br/>
|nb_photos | How many pictures in the ad. | 3 |<br/>
|surface | Living space in square meters. | 95 |<br/>
|dpeL | Note of the Energy performance diagnosis in letter (positioning in consumption) - Letter from A to G. | A |<br/>
|dpeC | Note of the Energy performance diagnosis (positioning in greenhouse gases) - Number included in a scale associated with the dpeL.| 50 |<br/>
|description | Ad body with infos about the housing. | Situé à Bordeaux, le bien propose... |<br/>
|prix | Monthly rent, charges included, in euros. | 750 |<br/>

<br/>

Particular Datas explanation :

<ul>
<li>typedebien : Type of the housing</li>
    <ul>
        <li>Appartement</li>
        <li>Maison / Villa</li>
    </ul><br/>
<li>idtypechauffage : Characteristics of property heating (if heating)</li>
    <ul>
        <li>individuel gaz</li>
        <li>électrique</li>
        <li>individuel électrique radiateur</li>
        <li>individuel gaz radiateur</li>
        <li>central</li>
        <li>individuel électrique</li>
        <li>central électrique sol</li>
        <li>individuel</li>
        <li>électrique radiateur</li>
        <li>central électrique mixte</li>
        <li>gaz collectif radiateur</li>
        <li>central radiateur</li>
        <li>gaz collectif</li>
        <li>individuel radiateur</li>
        <li>gaz</li>
        <li>central électrique</li>
        <li>gaz radiateur</li>
        <li>central électrique radiateur</li>
        <li>climatisation réversible individuelle</li>
        <li>radiateur</li>
        <li>gaz collectif sol</li>
        <li>individuel fuel radiateur</li>
        <li>climatisation réversible</li>
        <li>climatisation réversible centrale</li>
        <li>central fuel</li>
        <li>gaz collectif mixte</li>
    </ul><br/>
<li>idtypecuisine : Presence of a kitchen or not.</li>
    <ul>
        <li>américaine équipée</li>
        <li>séparée</li>
        <li>équipée</li>
        <li>américaine</li>
        <li>coin cuisine</li>
        <li>aucune</li>
        <li>séparée équipée</li>
        <li>coin cuisine équipé</li>
    </ul><br/>
<li>dpeC : Note of the Energy performance diagnosis (positioning in greenhouse gases)</li>
    <ul>
        <li>A : 0 - 50</li>
        <li>B : 51 - 90</li>
        <li>C : 91 - 150</li>
        <li>D : 151 - 230</li>
        <li>E : 231 - 330</li>
        <li>F : 331 - 450</li>
        <li>G : 451 - ...</li>
    </ul><br/>
</ul>

--------

# DATABASE MODELS



## List of metric's values obtained from all models (created: [ICI](https://github.com/Simplon-IA-Bdx-1/realestate-guillaume-nicos-pierre-silvia/blob/dev/training_container/Model.py) )

[ 03-model-database.sql](https://github.com/Simplon-IA-Bdx-1/realestate-guillaume-nicos-pierre-silvia/tree/dev/BDD/init-db)

## Structure

|   Fields  |  Description  |  Example |
|     :---:    |      :---:      |         :---:         |
|model_name <br/> | Model name in pickle format | realestate-model-2020-18-03-15h19s-rmsle-0.187.pkl |<br/>
|r2 <br/> | Metric R2 | 0.794285 |<br/>
|rmse | Metric RMSE | 174.747 |<br/>
|msle | Metric MSLE | 0.0210851 |<br/>
|rmsle | Metric RMSLE | 0.145207 |<br/>
|mape | Metric MAPE | 0.0940355 |<br/>