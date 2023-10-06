from setuptools import setup,find_packages
from typing import List



PROJECT_NAME ='Housing-Predictor'
VERSION='0.0.1'
AUTHOR='TAMIL'
DESCRIPTION='This is a First Machine Learning Project'
PACKAGES=['housing']
REQUIREMENT_FILE_NAME='requirements.txt'

def get_requirements_list()->List[str]:
    '''
    Description: This function is going to return the name of libraries in the requirements.txt file
    '''
    with open (file=REQUIREMENT_FILE_NAME,mode='r') as f:
        return f.readlines().remove('-e .')

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(), #['Housing'] folders name which has __init__.py
    install_requires=get_requirements_list()
)

if __name__=='__main__':
    print(get_requirements_list())