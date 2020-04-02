import argparse
from azureml.core import Run, Dataset
from os import path, makedirs
import numpy as np
import pandas as pd
from sklearn.svm import SVR
from datetime import datetime
from joblib import dump, load

dataset_dir = './datasets'
model_dir = './models'

parser = argparse.ArgumentParser(description='Train a model')
parser.add_argument('--dataset', required=True)
parser.add_argument('--model', required=True)

args = parser.parse_args()

run_context = Run.get_context()
input_dataset = run_context.input_datasets[args.dataset]
df_train = input_dataset.to_pandas_dataframe()

target_column = "prix"
X_train = df_train.drop(target_column, axis=1)
y_train = df_train[target_column]

svrRegressor = SVR(kernel='rbf', C=0.8)
svrRegressor.fit(X_train,y_train)

now = datetime.now()
model_file_name = 'realestate-model-' + now.strftime("%Y-%d-%m-%Hh%Mm") + '.pkl'

model_path = path.join(model_dir, model_file_name)
dump(svrRegressor, model_path)