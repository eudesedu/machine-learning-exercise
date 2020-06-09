import os
import getpass 

def f_env_config():
    """
    The environment configuration is a dictionary of path directory and URL.
    """
    # Website set:
    os.environ['CANCEL_CARD_URL'] = 'https://drive.google.com/file/d/1CHaMn8YPsbWaHeDDBONl2amk3YHq634G/view?usp=sharing'

    # Local dataset directory:
    os.environ['DIR_DATASET'] = 'C:\\Users\\eudes\\Documents\\github\\dataset'

f_env_config()
