import argparse
from azureml.core import Run, Dataset, Model
from os import path, makedirs
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import cross_val_score
import joblib

dataset_dir = './datasets'
model_dir = './models'

parser = argparse.ArgumentParser(description='model evaluation')
parser.add_argument('--dataset', required=True)
parser.add_argument('--model', required=True)

args = parser.parse_args()

model_path = Model.get_model_path(args.model)

model = joblib.load(open(model_path, 'rb'))

run_context = Run.get_context()

input_dataset = run_context.input_datasets[args.dataset]
valid_df = input_dataset.to_pandas_dataframe()

target_column = "prix"
X_valid = valid_df.drop(target_column, axis=1)
y_valid = valid_df[target_column]

y_valid_pred = model.predict(X_valid)
valid_r2 = r2_score(y_valid, y_valid_pred)
valid_rmse = np.sqrt(mean_squared_error(y_valid, y_valid_pred))
valid_rmsle = np.sqrt(mean_squared_error(np.log(y_valid),
                                         np.log(y_valid_pred)))
valid_msle = (mean_squared_error(np.log(y_valid), np.log(y_valid_pred)))
valid_mape = np.mean(np.abs((y_valid-y_valid_pred)/y_valid))

run_context.log('rmse', valid_rmse, description='Root mean square error on the validation set')
run_context.log('r2', valid_r2, description='Root square on the validation set')
run_context.log('rmsle', valid_rmsle, description='Root mean square log error on the validation set')
run_context.log('msle', valid_msle, description='Mean square log error on the validation set')
run_context.log('mape', valid_mape, description='Mean absolute percentage error on the validation set')

