import argparse
from azureml.core import Run, Dataset
from os import path, makedirs
import numpy as np
import pandas as pd

output_dir = './outputs'

parser = argparse.ArgumentParser(description='clean a dataset')
parser.add_argument('--input', required=True)
parser.add_argument('--output', required=True)

args = parser.parse_args()

run_context = Run.get_context()
input_dataset = run_context.input_datasets[args.input]

print(f"input dataset: {input_dataset}")

if isinstance(input_dataset, str):
    df_full = pd.read_csv(input_dataset, engine='python')
else:
    df_full = input_dataset.to_pandas_dataframe()

chauffageNArows = (df_full['idtypechauffage'] == '0') | (df_full['idtypechauffage'] == '') | (df_full['idtypechauffage'] == 'l')
df_full.loc[chauffageNArows,'idtypechauffage'] = np.nan
df_full['idtypechauffage'] = df_full['idtypechauffage'].replace(r'^z','gaz', regex=True)

codpostal33rows = df_full['codepostal'] == 33
df_full.loc[codpostal33rows,'codepostal'] = 33000

cuisineNArows = (df_full['idtypecuisine'] == '0') | (df_full['idtypecuisine'] == '')
df_full.loc[cuisineNArows,'idtypecuisine'] = np.nan
df_full['idtypecuisine'] = df_full['idtypecuisine'].replace(r'^éparée','séparée', regex=True)


nonzero_surface = (df_full['surface'] != '0') & (df_full['surface'] != '')
df_full = df_full[nonzero_surface]
df_full['surface'] = df_full['surface'].str.replace(",", ".").astype(float)

notcolocation_rows = ~(df_full['description'].str.contains("([Cc]oloc)")).astype('Bool')
df_full = df_full.loc[notcolocation_rows, :]

df_full = df_full.drop(['id', 'ville', 'codeinsee', 'nb_photos', 'dpeL',
                        'description'], axis=1)

makedirs(output_dir, exist_ok=True)

df_full.to_csv(path.join(output_dir, args.output))

