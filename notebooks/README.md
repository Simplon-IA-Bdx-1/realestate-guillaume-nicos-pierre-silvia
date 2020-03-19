# DATA PROCESSING

<p align="center"><img width=75% src="https://zupimages.net/up/20/12/shb4.png"></p>
<br/>

## :one: STEPS FROM [MODEL.ipynb](https://github.com/Simplon-IA-Bdx-1/realestate-guillaume-nicos-pierre-silvia/blob/dev/notebooks/Model.ipynb)

```
NOTEBOOK TO CREATE THE MODEL
```


### **1. Cleaning**
### **2. Pipeline**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Categorical features<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Binary features<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Numerical features<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Preprocessing pipe<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Output processing<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Regression model<br/>
### **3. Training and Evaluation**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Mean Regressor baseline<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Cross validation<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Valid evaluation<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Train evaluation<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Error analysis<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Export model<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Export metrics and insertion in the BDD<br/>
<br/>

--------------------------
## :two: [PREDICTION.ipynb](https://github.com/Simplon-IA-Bdx-1/realestate-guillaume-nicos-pierre-silvia/blob/dev/notebooks/Prediction.ipynb)

```
NOTEBOOK TO MAKE THE PREDICTION FROM THE MODEL NOTEBOOK (SEE ABOVE)
```


Picked features for the prediction :

* typedebien
* codepostal
* idtypechauffage
* idtypecuisine
* si_balcon
* nb_chambres
* nb_pieces
* si_sdbain
* si_sdEau
* etage
* surface
* dpeC