import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO,format=" %(asctime)s : %(levelname)s : %(message)s ")

def create_directory_and_files(list_of_files:list[str]) :

    # Create the main directory
    for f in list_of_files :
        f = Path(f)
        d,file_name = os.path.split(f)
        if d != "":
            
            os.makedirs(d,exist_ok=True)
            logging.info(f"Created main directory: {f}")
        if (not os.path.exists(f)) or (not os.path.getsize(f)):
            with open(f, 'w') as f:
                logging.info(f"Created file: {file_name}")
                pass
        else:
            logging.info(f"File '{file_name}' already exists and is not empty.")
            print(f"File '{file_name}' already exists and is not empty.")

project_name = ""
while True:
    project_name = input("enter a project name : ")
    if project_name:
        break

list_of_files = [

    f"src/{project_name}/__init__.py",
    f".github/workflows/.gitkeep",
    f"tests/integration/__init__.py",
    f"tests/unit/__init__.py",
    "setup.py",
    "setup.cfg",
    "tox.ini",
    "pyproject.toml",
    "requirements_dev.txt",
    "requirements.txt",
    "init_setup.sh"

]

create_directory_and_files(list_of_files)
    
