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
input_dataset = run_context.input_datasets[args.dataset]
fulltrain = input_dataset.to_pandas_dataframe()

train_size = int(args.trainsize)
valid_size = int(args.validsize)

#valid_size = int(validsize)
#train_size = int(len(input_dataset) - valid_size)

if args.train:
    train = fulltrain[-train_size-valid_size:-valid_size]
    train.to_csv(path.join(output_dir, args.train))
valid = fulltrain[-valid_size:]
valid.to_csv(path.join(output_dir, args.valid))

print('Dataset:  {}'.format(input_dataset))
print('Train name:  {}'.format(train))
print('Valid name:  {}'.format(valid))
print('Train size:  {}'.format(train_size))
print('Valid size:  {}'.format(valid_size))

