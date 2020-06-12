import pandas as pd
import numpy as np
import argparse
import importlib
import os
import sys

def f_load_dataset_local(setwd):
    """
    Local dataset of credit cards canceled.
    """
    os.chdir(setwd)
    d_cancel_card = pd.read_csv('cartao-credito-cancelamento.csv').drop(columns=['ID'], axis=1)
    return print(d_cancel_card, 
                 d_cancel_card.dtypes,  
                 d_cancel_card.columns,
                 d_cancel_card.corr(),
                 d_cancel_card.isnull().sum(),
                 d_cancel_card.nunique(),
                 d_cancel_card.shape)

def f_main():
    """
    Import a module to generate the environment configuration and parser argument.
    """
    descr = """
        Define the parser argument to load a local dataset.
    """
    parser = argparse.ArgumentParser(description=descr)
    parser.add_argument('-load_dataset_local',
                        dest='load_dataset_local',
                        action='store_const',
                        const=True,
                        help='Call the f_load_dataset_local function')
    cmd_args = parser.parse_args()

    importlib.import_module('mod-environment')
    if cmd_args.load_dataset_local: 
        f_load_dataset_local(os.environ.get('DIR_DATASET'))

if __name__ == '__main__':
    f_main()
    sys.exit(0)
