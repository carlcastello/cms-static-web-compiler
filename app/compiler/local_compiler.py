import os
import logging

from app.compiler import Compiler

class LocalCompiler(Compiler):

    def __init__(self, project_name: str, **kwargs: dict) -> None:
        super().__init__(project_name)
        self._output_path = kwargs.get('output_path', '../static-websites/')

    def create_project_directories(self) -> None:
        for key in self._generate_project_keys():
            path = self._output_path + key
            if os.path.isfile(path):
                os.makedirs(path)
                continue
            logging.warning('Directory "{}" already exist.'.format(key))