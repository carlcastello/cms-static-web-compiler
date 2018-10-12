"""
    Holds Compiler related classes, functions and constants that are
    used specifically for local environment
"""

import os
import logging

from app.compiler import Compiler

class LocalCompiler(Compiler):
    """
        Implementation of the abstract class for the local environment
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
            if os.path.isfile(path):
                os.makedirs(path)
                continue
            logging.warning('Directory "%s" already exist.', key)
