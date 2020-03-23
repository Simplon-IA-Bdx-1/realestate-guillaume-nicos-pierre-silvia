from flask import Flask, render_template, request, jsonify
import joblib
import logging as log
from pandas import DataFrame
from os import path, getcwd, getenv
from glob import glob
import mysql.connector
#from dotenv import load_dotenv

app = Flask(__name__)


def connectToDatabase():
    #load_dotenv()
    return mysql.connector.connect(
        user=getenv("MYSQL_USER"),
        password=getenv("MYSQL_PASSWORD"),
        host=getenv("MYSQL_HOST"),
        database=getenv("MYSQL_DATABASE")
    )



def disconnectDatabase(cnx):
    cnx.close()

def get_current_model(cnx):
    cursor = cnx.cursor(dictionary=True)
    cursor.execute("SELECT m.* FROM `models` AS m JOIN `current_model` AS c ON m.model_name = c.model_name")
    result = cursor.fetchone()
    cursor.close()
    disconnectDatabase(cnx)
    return result

    return get_current_model(cnx)['model_name']

@app.route('/')
def hello_world():
    return render_template('formulaire.html')


@app.route('/model/list', methods=['GET'])
def list_models():
    cnx = connectToDatabase()
    cursor = cnx.cursor(dictionary=True)
    cursor.execute("SELECT * FROM `models`")
    results = cursor.fetchall()
    model_list = {}
    for result in results:
        model_list[result['model_name']] = result
        del model_list[result['model_name']]['model_name']
    cursor.close()
    disconnectDatabase(cnx)
    return jsonify({'status': 'OK',
                    'result': model_list},
                   200)

@app.route('/model/current', methods=['GET'])
def current_model():
    cnx = connectToDatabase()
    result = get_current_model(cnx)
    disconnectDatabase(cnx)
    return jsonify({'status': 'OK',
                    'result': result},
                   200)

@app.route('/model/set', methods=['POST'])
def set_model():
    global model
    model_name = request.form['model_name']
    app.logger.info(model_name)
    cnx = connectToDatabase()
    cursor = cnx.cursor()
    cursor.execute(f"SELECT `model_name` FROM `models` WHERE `model_name` = '{model_name}' LIMIT 1")
    result = cursor.fetchone()
    if result is None:
        cursor.close()
        disconnectDatabase(cnx)
        return jsonify({'status': 'Model does not exist', },
                       400)
    
    cursor.close()
    cursor = cnx.cursor()
    cursor.execute(f"""INSERT into `current_model` SELECT '1' ,`model_name` FROM models WHERE `model_name` = '{model_name}'
ON DUPLICATE KEY UPDATE `model_name` = models.`model_name`""")
    cnx.commit()
    cursor.close()
    disconnectDatabase(cnx)
    file_path = path.join('/app/www/models', model_name)
    model = joblib.load(open(file_path, 'rb'))
    return jsonify({'statut': 'OK'}, 200)

@app.route('/predict', methods=['POST'])
def predict():
    global model
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
    
    #file_path = max(glob(path.join('/app/www/models', 'realestate-model-*.pkl')))    
    #model = joblib.load(open(file_path, 'rb'))
    output = round(model.predict(values)[0],0)

    return render_template('resultats.html', prix = output, typedebien = request.form['typedebien'])

@app.route('/api', methods=['GET'])
def predict_api():
    global model
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
    
    #file_path = max(glob(path.join('/app/www/models', 'realestate-model-*.pkl')))    
    #model = joblib.load(open(file_path, 'rb'))
    output = round(model.predict(values)[0],0)
    
    return jsonify({
        'statut' : 'OK',
        'prix' : output
    },
    200
    )


if __name__ == '__main__':
    cnx = connectToDatabase()
    # cursor = cnx.cursor()
    # cursor.execute("SELECT `model_name` FROM `current_model` LIMIT 1")
    # result = cursor.fetchone()
    # cursor.close()
    result = get_current_model(cnx)
    if result is None:
        cursor = cnx.cursor()
        cursor.execute("SELECT `model_name` FROM `models` ORDER BY `model_name` DESC LIMIT 1")
        result = cursor.fetchone()
    disconnectDatabase(cnx)
    model_name = result['model_name']
    #log.info(model_name)
    file_path = path.join('/app/www/models', model_name)
    model = joblib.load(open(file_path, 'rb'))
    app.run(debug=True, host='0.0.0.0')
