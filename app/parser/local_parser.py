"""
Holds Parser related classes, functions and constants that are
used specifically for local environment
"""
from json import load
import logging
from typing import Dict, Any

from app.parser import Parser

class LocalParser(Parser):
    """
    Implementation of the Parser class using the local os directory
    """
    def __init__(self, project_name: str, **kwargs) -> None:
        super().__init__(project_name, **kwargs)

        self._location: str = f'../json-websites/{project_name}.json'

    def get_project_data(self) -> Dict[str, Any]:
        """
        Fetching project data in the local directory
        """
        try:
            with open(self._location) as json_data:
                return load(json_data)
        except FileNotFoundError:
            logging.warning('No such file or directory: "%s"', self._location)
            return {}
