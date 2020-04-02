import argparse
from azureml.core import Run, Dataset
from os import path, makedirs
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import cross_val_score
from joblib import load

dataset_dir = './datasets'
model_dir = './models'

parser = argparse.ArgumentParser(description='model evaluation')
parser.add_argument('--dataset', required=True)
parser.add_argument('--model', required=True)

args = parser.parse_args()

model_path = Model.get_model_path(args.model)
model = joblib.load(model_path)

run_context = Run.get_context()
evaluation = run_context.log('rmse', valid_rmse, description='Root mean square error on the validation set')
input_dataset = run_context.input_datasets[args.dataset]
model = input_dataset.to_pandas_dataframe()


scores = cross_val_score(full_pipe, X_fulltrain, y=y_fulltrain, cv=10)

y_valid_pred = full_pipe.predict(X_valid)
valid_r2 = r2_score(y_valid, y_valid_pred)
valid_rmse = np.sqrt(mean_squared_error(y_valid, y_valid_pred))
valid_rmsle = np.sqrt(mean_squared_error(np.log(y_valid),
                                         np.log(y_valid_pred)))
valid_msle = (mean_squared_error(np.log(y_valid), np.log(y_valid_pred)))
valid_mape = np.mean(np.abs((y_valid-y_valid_pred)/y_valid))


model_file_name = 'realestate-model-'\
                  + now.strftime("%Y-%d-%m-%Hh%Mm")\
                  + '-mape-'\
                  + '{:.3f}'.format(valid_mape)\
                  + '.pkl'

