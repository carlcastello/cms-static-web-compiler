import os

from . import Parser

class LocalParser(Parser):

    def __init__(self, project_name: str, **kwargs: dict) -> None:
        super().__init__(project_name)
        self._output_path = kwargs.get('output_path', '../static-websites/')

    def create_project_directories(self) -> None:
        for key in self.generate_project_keys():
            os.makedirs(self._output_path + key)
