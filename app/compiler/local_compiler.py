"""
Holds Compiler related classes, functions and constants that are
used specifically for local environment
"""

import os
import logging

from app.compiler import Compiler

class LocalCompiler(Compiler):
    """
    Implementation of the Compiler class using the local os directory
    """
    # pylint: disable=too-few-public-methods

    def __init__(self, project_name: str, **kwargs: str) -> None:
        """
        :project_name: Name of the project/root folder
        :kwargs: Extra arguments needed for this compiler
        """
        super().__init__(project_name)
        self._output_path: str = kwargs.get('output_path', '../static-websites')

    def create_project_directories(self) -> None:
        """
        Creates folders/directories of a project
        """
        for key in self._generate_project_keys():
            path: str = f'{self._output_path}/{key}'
            if not os.path.isdir(path):
                os.makedirs(path)
                continue
            logging.warning('Directory "%s" already exist.', path)

    def _save_file(self, file_location: str, file_content: str, in_binary: bool=False) -> None:
        with open(f'{self._output_path}/{file_location}', 'wb' if in_binary else 'w') as file:
            file.write(file_content)
