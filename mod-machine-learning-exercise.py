import pandas as pd
import numpy as np
import argparse
import importlib
import os
import sys

def f_load_dataset(url, path):
    """
    Public datasets (via Google Drive) of credit cards canceled.
    """
    #d_cancel_card = Socrata(url, token, email, password).get(tag, limit=3)
    #d_crime_sample = pd.DataFrame.from_records(d_crime_socrata)
    #return print(d_crime_sample)

def f_main():
    """
    Automated execution to generate the environment configuration and parser argument.
    """
    descr = """
        Define the parser argument to load a dataset via Google Drive.
    """
    parser = argparse.ArgumentParser(description=descr)
    parser.add_argument('-load_dataset_googledrive', 
                        dest='load_dataset_googledrive', 
                        action='store_const', 
                        const=True, 
                        help='Call the f_load_dataset function')
    cmd_args = parser.parse_args()

    # The environment configuration is a dictionary of path directory and URL.
    importlib.import_module('mod-environment')
    if cmd_args.load_dataset_googledrive: 
        f_load_dataset(os.environ.get('CANCEL_CARD_URL'), os.environ.get('DIR_DATASET'))

if __name__ == '__main__':
    f_main()
    sys.exit(0)
