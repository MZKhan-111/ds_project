import os
import yaml
from src.datascience.utils import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Dict, Any, Union
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read yaml file
    Args:
        path_to_yaml (str): path to yaml file

    Raises:
        valueError: if the file is empty

    Return: 
        ConfigBox object
    """
    try:
        with open(path_to_yaml) as file:
            content = yaml.safe_load(file)
            logger.info(f"Reading the yaml file: {path_to_yaml}")
        return ConfigBox(content)
    except BoxValueError:
        logger.error(f"Empty file: {path_to_yaml}")
        raise ValueError(f"Empty file: {path_to_yaml}")
    except Exception as e:
        logger.error(f"Error reading the yaml file: {path_to_yaml}")
        raise e
    

@ensure_annotations
def create_directories(path_to_directory: list, verbose=True):
    """
    Create list of directories
    Args:
        path_to_directory (list): list of path to directory
        ignore_log (bool, optional): ignore if multiple directories are created. Defaults to True.
    """
    try:
        os.makedirs(path_to_directory, exist_ok=True)
        logger.info(f"Creating directory: {path_to_directory}")
    except Exception as e:
        logger.error(f"Error creating directory: {path_to_directory}")
        raise e
