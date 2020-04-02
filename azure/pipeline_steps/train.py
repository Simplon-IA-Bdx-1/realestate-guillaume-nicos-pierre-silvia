import argparse
from azureml.core import Run, Dataset
from os import path, makedirs
import numpy as np
#import pandas as pd
from sklearn.svm import SVR
#from datetime import datetime
from joblib import dump, load
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import (StandardScaler, LabelEncoder, PolynomialFeatures,
                                   OneHotEncoder, OrdinalEncoder, FunctionTransformer,
                                   PowerTransformer)
from sklearn.compose import ColumnTransformer, TransformedTargetRegressor

output_dir = './outputs'

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

categoricals = ['typedebien', 'idtypechauffage', 'idtypecuisine', 'codepostal']
binaries = ['si_balcon', 'si_sdbain', 'si_sdEau']
numericals = ['nb_chambres', 'nb_pieces', 'etage', 'surface', 'dpeC']
text = ['description']

categorical_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown="ignore"))
])

binary_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent'))
])

numerical_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    # ('poly', PolynomialFeatures(degree=2)),
    ('power',  PowerTransformer()),
    # ('scaler', StandardScaler())
])

preprocess_pipe = ColumnTransformer([
    ('cat', categorical_pipe, categoricals),
    ('num', numerical_pipe, numericals),
    ('ord', binary_pipe, binaries)
])

output_pipe = Pipeline([
    ('log', FunctionTransformer(func=np.log, inverse_func=np.exp)),
    ('scaler', StandardScaler())
])

svrRegressor = SVR(kernel='rbf', C=0.8)

model = Pipeline([
    ('pre', preprocess_pipe),
    ('reg', svrRegressor)
])

full_pipe = TransformedTargetRegressor(regressor=model, transformer=output_pipe)

full_pipe.fit(X_train,y_train);

makedirs(output_dir, exist_ok=True)
model_path = path.join(output_dir, args.model)
dump(full_pipe, model_path)
