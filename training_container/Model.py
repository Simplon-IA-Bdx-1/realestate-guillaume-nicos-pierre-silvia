#!/usr/bin/env python3
# coding: utf-8

from pandas import DataFrame, read_csv
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import (StandardScaler, LabelEncoder, PolynomialFeatures,
                                   OneHotEncoder, OrdinalEncoder, FunctionTransformer,
                                   PowerTransformer)
from sklearn.compose import ColumnTransformer, TransformedTargetRegressor
from sklearn.linear_model import Ridge
from xgboost import XGBRegressor
from sklearn.svm import SVR
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import cross_val_score
from joblib import dump, load
#import seaborn as sns
#import matplotlib.pyplot as plt
from datetime import datetime

import numpy as np
from query import  get_all_annonces,  connectToDatabase,  disconnectDatabase
from annonce import Annonce, to_csv
from os import getcwd, mkdir, path

now = datetime.now()
base_dir = path.dirname(getcwd())
model_dir = base_dir + '/models'
if not path.exists(model_dir):
    mkdir(model_dir)
csv_filename = 'fulltrain-' + now.strftime("%Y-%d-%m-%Hh%Mm") + '.csv'
csv_path = path.join(model_dir, csv_filename)

print("retrieving dataset from database")
cnx = connectToDatabase()
to_csv(csv_path, get_all_annonces(cnx))
print("Done")
SEED=42

#get_ipython().system('../scrapper/scrapper.py csv --file ./fulltrain.csv')

print("cleaning dataset")
df_full = read_csv(csv_path, index_col='idannonce')

chauffageNArows = df_full['idtypechauffage'] == 0
df_full.loc[chauffageNArows,'idtypechauffage'] = np.nan

codpostal33rows = df_full['codepostal'] == 33
df_full.loc[codpostal33rows,'codepostal'] = 33000

cuisineNArows = df_full['idtypecuisine'] == 0
df_full.loc[cuisineNArows,'idtypecuisine'] = np.nan

df_full['surface'] = df_full['surface'].str.replace(",", ".").astype(float)

nonzero_surface = df_full['surface'] != 0
df_full = df_full.loc[nonzero_surface, :]

notcolocation_rows = ~(df_full['description'].str.contains("([Cc]oloc)")).astype('Bool')
df_full = df_full.loc[notcolocation_rows, :]

df_full = df_full.drop(['id', 'ville', 'codeinsee', 'nb_photos', 'dpeL',
                        'description'], axis=1)

# df_full.to_csv('dataset_clean.csv', header=True, index_label=id)

# categoricals = ['typedebien', 'ville','idtypechauffage', 'idtypecuisine','codepostal','codeinsee']
categoricals = ['typedebien', 'idtypechauffage', 'idtypecuisine', 'codepostal']
binaries = ['si_balcon', 'si_sdbain', 'si_sdEau']
# numericals = ['nb_chambres', 'nb_pieces', 'nb_photos', 'etage', 'surface', 'dpeC']
numericals = ['nb_chambres', 'nb_pieces', 'etage', 'surface', 'dpeC']
text = ['description']
print("Done")

# ### Categorical features

#for col in categoricals:
#    print(df_full[col].unique())

categorical_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown="ignore"))
])

# ### Binary features

#for col in binaries:
#    print(df_full[col].unique())

binary_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent'))
])


# ### Numerical features

numerical_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    # ('poly', PolynomialFeatures(degree=2)),
    ('power',  PowerTransformer()),
    # ('scaler', StandardScaler())
])


# ### preprocessing pipe

# In[22]:


preprocess_pipe = ColumnTransformer([
    ('cat', categorical_pipe, categoricals),
    ('num', numerical_pipe, numericals),
    ('ord', binary_pipe, binaries)
])


# ### output processing

# In[23]:


output_pipe = Pipeline([
    ('log', FunctionTransformer(func=np.log, inverse_func=np.exp)),
    ('scaler', StandardScaler())
])


# ### regression model

# In[24]:


#rdgRegressor = Ridge()
#xgbRegressor = XGBRegressor(booster="gbtree")
svrRegressor = SVR(kernel='rbf', C=0.8)


# In[25]:


model = Pipeline([
    ('pre', preprocess_pipe),
    ('reg', svrRegressor)
])


# In[26]:


full_pipe = TransformedTargetRegressor(regressor=model, transformer=output_pipe)

#dump(full_pipe,'pipeline-model.joblib')

from sklearn.model_selection import train_test_split
target_column = "prix"

X_fulltrain = df_full.drop(target_column, axis=1)
y_fulltrain = df_full[target_column]

print("training")
X_train, X_valid, y_train, y_valid = train_test_split(X_fulltrain, y_fulltrain, test_size=0.2, random_state=SEED)


# ## Training and evaluation

# In[29]:


full_pipe.fit(X_train,y_train);
print("Done")

# ### Mean regressor baseline

# In[30]:


#y_valid_pred = [np.mean(y_train)] * y_valid.shape[0]
#r2 = r2_score(y_valid, y_valid_pred)
#rmse = np.sqrt(mean_squared_error(y_valid, y_valid_pred))
#rmsle = np.sqrt(mean_squared_error(np.log(y_valid), np.log(y_valid_pred)))
#msle = (mean_squared_error(np.log(y_valid), np.log(y_valid_pred)))
#mape = np.mean(np.abs((y_valid-y_valid_pred)/y_valid))
#print(f"    r2 = {r2}\nrmse = {rmse}\nmsle = {msle}\nrmsle = {rmsle}\nmape = {mape}")


# ### Cross validation

# In[31]:

print("cross validation:")
scores = cross_val_score(full_pipe, X_fulltrain, y=y_fulltrain, cv=10)
print(f'    mean R2 = {np.mean(scores)} +/- {np.std(scores)}')
#scores


# ### Valid evaluation
print("evaluating:")
y_valid_pred = full_pipe.predict(X_valid)
valid_r2 = r2_score(y_valid, y_valid_pred)
valid_rmse = np.sqrt(mean_squared_error(y_valid, y_valid_pred))
valid_rmsle = np.sqrt(mean_squared_error(np.log(y_valid),
                                         np.log(y_valid_pred)))
valid_msle = (mean_squared_error(np.log(y_valid), np.log(y_valid_pred)))
valid_mape = np.mean(np.abs((y_valid-y_valid_pred)/y_valid))

print(f'\tr2 = {valid_r2}\n\trmse = {valid_rmse}\n\tmsle = {valid_msle}\n\trmsle = {valid_rmsle}\n\tmape = {valid_mape}')
#grid = sns.JointGrid(y_valid, y_valid_pred)
#grid = grid.plot(sns.regplot, sns.distplot)
#grid.ax_joint.plot([0,2500], [0,2500], 'r');


# ### Train evaluation

# In[33]:


#y_train_pred = full_pipe.predict(X_train)
#r2 = r2_score(y_train, y_train_pred)
#rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
#rmsle = np.sqrt(mean_squared_error(np.log(y_train), np.log(y_train_pred)))
#msle = (mean_squared_error(np.log(y_train), np.log(y_train_pred)))
#mape = np.mean(np.abs((y_train-y_train_pred)/y_train))
#print(f'r2 = {r2}\nrmse = {rmse}\nmsle = {msle}\nrmsle = {rmsle}\nmape = {mape}')
#grid = sns.JointGrid(y_train, y_train_pred)
#grid = grid.plot(sns.regplot, sns.distplot)
#grid.ax_joint.plot([0,2500], [0,2500], 'r');

# ## export model

model_file_name = 'realestate-model-'\
                  + now.strftime("%Y-%d-%m-%Hh%Mm")\
                  + '-mape-'\
                  + '{:.3f}'.format(valid_mape)\
                  + '.pkl'


model_path = path.join(model_dir, model_file_name)
model_path

print("saving model:")
dump(full_pipe, model_path)
print(f"    {model_file_name}")

#from glob import glob
#max(glob(path.join(model_dir, 'realestate-model-*.pkl')))

# ## metrics into database

import mysql.connector
from dotenv import load_dotenv
from os import getenv


def connectToDatabase():
    load_dotenv()
    return mysql.connector.connect(
        user=getenv("MYSQL_USER"),
        password=getenv("MYSQL_PASSWORD"),
        host=getenv("MYSQL_HOST"),
        database=getenv("MYSQL_DATABASE")
    )


def createCursor(cnx):
    return cnx.cursor(dictionary=True)


def insertModelQuery(model_name,r2,rmse,rmsle, msle, mape):
    return ("INSERT INTO `models` (`model_name`, `r2`,`rmse`, `rmsle`,`msle`, `mape`) VALUES ('{}', '{}','{}', '{}','{}', '{}')".format(model_name,r2,rmse,rmsle, msle, mape))


def closeCursor(cursor):
    cursor.close()


def disconnectDatabase(cnx):
    cnx.close()


print("saving metrics to database")
cnx = connectToDatabase()
cursor = createCursor(cnx)
cursor.execute(insertModelQuery(model_file_name, valid_r2, valid_rmse,
                                valid_rmsle, valid_msle, valid_mape))
cnx.commit()
closeCursor(cursor)
disconnectDatabase(cnx)
print("Done")
