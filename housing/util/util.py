import yaml
import os
from housing.exception import HousingException

def read_yaml_file(filepath:str)->dict:
    '''
    Reads a YAML file and return the contents as a dictionary
    '''
    try:
        with open (file=filepath,mode='rb') as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise HousingException(e,sys) from e