"""
Holds Compiler related classes, functions and constants that are
used specifically for local environment
"""

import os
import logging

from app.constants import MARKUP
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
        self._output_path: str = kwargs.get('output_path', '../static-websites/')

    def create_project_directories(self) -> None:
        """
        Creates folders/directories of a project
        """
        for key in self._generate_project_keys():
            path: str = self._output_path + key
            if not os.path.isdir(path):
                os.makedirs(path)
                continue
            logging.warning('Directory "%s" already exist.', path)

    def create_project_files(self, project_files) -> None:
        """
            Creates HTML pages for the projects based on a json object
        """
        def _compile_markup(files):
            for file_name, file_content in files.items():
                file_location = self._output_path + '{}/{}/{}'.format(self._project_name, environment, file_name)
                file = open(file_location, 'w')
                file.write(file_content)
                file.close()

        for environment in self._environments:
            for file_category, files in project_files.items():
                if file_category == MARKUP:
                    _compile_markup(files)
