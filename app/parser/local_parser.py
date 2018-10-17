from json import load
import logging

from app.parser import Parser

class LocalParser(Parser):

    def __init__(self, project_name: str, **kwargs) -> None:
        super().__init__(project_name, **kwargs)

        self._location: str = '../json-websites/{}'.format(project_name)

    def _open_file(self) -> dict:
        try:
            with open(self._location.format(self._project_name)) as json_data:
                return load(json_data)
        except FileNotFoundError:
            logging.warning('No such file or directory: "%s"', self._location)
            return {}

    def read_project_data(self):
        """
            Fetching project data in the local directory
        """
        print(self._open_file())
