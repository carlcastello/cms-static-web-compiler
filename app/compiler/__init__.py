"""
Holds Compiler (memory to file) related classes, functions and constants that are
used by all environments
"""

from typing import List

from app.constants import IMAGES, CSS, JS, ROBOTS

class Compiler:
    """
    A compiler abstract class with common methods for all environments
    """
    # pylint: disable=too-few-public-methods

    _key_structure: str = "{}/{}/{}"
    _environments: List[str] = ['develop', 'production']
    _folders: List[str] = [CSS, IMAGES, JS, ROBOTS]

    def __init__(self, project_name: str) -> None:
        """
        :project_name: Name of the project/root folder
        """
        self._project_name: str = project_name

    def _generate_project_keys(self) -> List[str]:
        """
        Creates a directory tree
        """

        folder_keys: List[str] = []
        for environment in self._environments:
            for folder in self._folders:
                folder_keys.append(self._key_structure.format(
                    self._project_name,
                    environment,
                    folder
                ))

        return folder_keys

    def create_project_directories(self) -> None:
        """
        An abstract method intended to create folders/directories for a project.
        """
        raise NotImplementedError('Trying to run compiler without a given environment')

    def create_project_files(self, project_files) -> None:
        """
        An abstract method intended to create html pages based on a json object.
        """
        raise NotImplementedError('Trying to run compiler without a given environment')
