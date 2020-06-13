import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import argparse
import importlib
import os
import sys

def f_load_local_dataset(setwd):
    """
    Local dataset of credit cards canceled.
    """
    os.chdir(setwd)
    d_cancel_card = pd.read_csv('cartao-credito-cancelamento.csv').drop(columns=['ID'], axis=1)
    return print(d_cancel_card, d_cancel_card.dtypes, d_cancel_card.columns, d_cancel_card.corr(), d_cancel_card.isnull().sum(), d_cancel_card.nunique(), d_cancel_card.shape)

def f_get_dummy(setwd):
    """
    Generate dummy variables.
    """
    le = LabelEncoder()
    os.chdir(setwd)
    d_cancel_card = pd.read_csv('cartao-credito-cancelamento.csv').drop(columns=['ID'], axis=1)
    dummy_cancel_card = pd.get_dummies(d_cancel_card, columns=['PerfilEconomico', 'Sexo', 'PerfilCompra', 'RegiaodoPais'], drop_first=True)
    d_uf = pd.DataFrame(le.fit_transform(dummy_cancel_card['UF']), columns=['le_UF'])
    #d_cid = pd.DataFrame(le.fit_transform(dummy_cancel_card['CidadeResidencia']), columns=['LE_CidadeResidencia'])
    dummy_cancel_card = pd.merge(dummy_cancel_card, d_uf, left_index=True, right_index=True)
    return print(d_uf, 
                 dummy_cancel_card)

def f_main():
    """
    Import a module to generate the environment configuration and parser argument.
    """
    descr = """
        Define the parser argument to load a local dataset.
    """
    parser = argparse.ArgumentParser(description=descr)
    parser.add_argument('-load_local_dataset',
                        dest='load_local_dataset',
                        action='store_const',
                        const=True,
                        help='Call the f_load_local_dataset function')
    parser.add_argument('-get_dummy',
                        dest='get_dummy',
                        action='store_const',
                        const=True,
                        help='Call the f_get_dummy function')
    cmd_args = parser.parse_args()

    importlib.import_module('mod-environment')
    if cmd_args.load_local_dataset: 
        f_load_local_dataset(os.environ.get('DIR_DATASET'))
    if cmd_args.get_dummy: 
        f_get_dummy(os.environ.get('DIR_DATASET'))

if __name__ == '__main__':
    f_main()
    sys.exit(0)
