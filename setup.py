from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->list[str]:
    #it will read requirement.txt

    requirements=[]

    with open(file_path) as file_obj :
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]

    return requirements        



setup(
    
    name='mlproject',
    version='0.0.1',
    author="sattvik",
    author_email="sattviky@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')
)