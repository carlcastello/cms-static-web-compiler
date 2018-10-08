import os

from . import Parser

class LocalParser(Parser):

    def __init__(self, project_name: str, output_path: str) -> None:
        super().__init__(project_name)
        self._output_path = output_path

    def create_project_directories(self) -> None:
        for key in self.generate_project_keys():
            os.mkdir(self._output_path + key)
