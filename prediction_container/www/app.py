from flask import Flask, render_template, request, jsonify
import joblib
import logging as log
from pandas import DataFrame
from os import path, getcwd
from glob import glob

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('formulaire.html')

@app.route('/predict', methods=['POST'])
def predict():
    # log.info(request.form)
    input_list = [[
        request.form['typedebien'],
        request.form['codepostal'],
        request.form['idtypechauffage'],
        request.form['idtypecuisine'],
        request.form['si_balcon'],
        request.form['nb_chambres'],
        request.form['nb_pieces'],
        request.form['si_sdbain'],
        request.form['si_sdEau'],
        request.form['etage'],
        request.form['surface'],
        request.form['dpeC']
    ]]
    
    columns = ['typedebien', 'codepostal', 'idtypechauffage', 'idtypecuisine',
           'si_balcon', 'nb_chambres', 'nb_pieces', 'si_sdbain', 'si_sdEau',
           'etage', 'surface', 'dpeC']
    values = DataFrame(data=input_list,columns=columns)
    
    file_path = max(glob(path.join('/app/www/models', 'realestate-model-*.pkl')))    
    model = joblib.load(open(file_path, 'rb'))
    output = round(model.predict(values)[0],0)

    return render_template('resultats.html', prix = output, typedebien = request.form['typedebien'])

@app.route('/api', methods=['GET'])
def predict_api():
    input_list = [[
        request.json['typedebien'],
        request.json['codepostal'],
        request.json['idtypechauffage'],
        request.json['idtypecuisine'],
        request.json['si_balcon'],
        request.json['nb_chambres'],
        request.json['nb_pieces'],
        request.json['si_sdbain'],
        request.json['si_sdEau'],
        request.json['etage'],
        request.json['surface'],
        request.json['dpeC']
    ]]
    
    columns = ['typedebien', 'codepostal', 'idtypechauffage', 'idtypecuisine',
           'si_balcon', 'nb_chambres', 'nb_pieces', 'si_sdbain', 'si_sdEau',
           'etage', 'surface', 'dpeC']
    values = DataFrame(data=input_list,columns=columns)
    
    file_path = max(glob(path.join('/app/www/models', 'realestate-model-*.pkl')))    
    model = joblib.load(open(file_path, 'rb'))
    output = round(model.predict(values)[0],0)
    
    return jsonify({
        'statut' : 'OK',
        'prix' : output
    },
    200
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')