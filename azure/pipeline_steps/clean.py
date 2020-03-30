import argparse
from azureml.core import Run, Dataset
from os import path

output_dir = './Outputs'

parser = argparse.ArgumentParser(description='clean a dataset')
parser.add_argument('--input', required=True)
parser.add_argument('--output', required=True)

args = parser.parse_args()

run_context = Run.get_context()
input_dataset = run_context.input_datasets[args.input]
df_full = input_dataset.to_pandas_dataframe()

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

df_full.to_csv(path.join(output_dir, args.output))
