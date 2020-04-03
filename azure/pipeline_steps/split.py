import argparse
from azureml.core import Run, Dataset
from os import path, makedirs
import numpy as np
import pandas as pd

output_dir = './outputs'

parser = argparse.ArgumentParser(description='Split a dataset')
parser.add_argument('--dataset', required=True)
parser.add_argument('--train', required=False)
parser.add_argument('--valid', required=True)
parser.add_argument('--trainsize', required=False)
parser.add_argument('--validsize', required=True)

args = parser.parse_args()

run_context = Run.get_context()
print(f'dataset name: {args.dataset}')
input_dataset = run_context.input_datasets[args.dataset]
print(f'input: {input_dataset}')
print(f'type: {type(input_dataset)}')

if isinstance(input_dataset, str):
    fulltrain = pd.read_csv(input_dataset)
else:
    fulltrain = input_dataset.to_pandas_dataframe()

print(f"fulltrain shape: {fulltrain.shape}")

train_size = int(args.trainsize)
valid_size = int(args.validsize)

# valid_size = int(validsize)
# train_size = int(len(input_dataset) - valid_size)

if args.train:
    train = fulltrain[-train_size-valid_size:-valid_size]
    train.to_csv(path.join(output_dir, args.train))
    print('Train size:  {}'.format(train.shape))
valid = fulltrain[-valid_size:]
valid.to_csv(path.join(output_dir, args.valid))
print('Valid size:  {}'.format(valid.shape))
