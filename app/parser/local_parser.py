from json import load
import logging

from app.parser import Parser

class LocalParser(Parser):

    def __init__(self, project_name: str, **kwargs) -> None:
        super().__init__(project_name, **kwargs)

        self._location: str = '../json-websites/{}.json'.format(project_name)

    def get_project_data(self) -> dict:
        """
        Fetching project data in the local directory
        """
        try:
            with open(self._location.format(self._project_name)) as json_data:
                return load(json_data)
        except FileNotFoundError:
            logging.warning('No such file or directory: "%s"', self._location)
            return {}
