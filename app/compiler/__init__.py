"""
Holds Compiler (json to html) related classes, functions and constants that are
used by all environments
"""

from typing import List, Dict

class Compiler:
    """
    A compiler abstract class with common methods for all environments
    """
    # pylint: disable=too-few-public-methods

    def __init__(self, project_name: str) -> None:
        """
        :project_name: Name of the project/root folder
        """
        self._project_name: str = project_name

    def _generate_project_keys(self) -> List[str]:
        """
        Creates a directory tree
        """
        key_structure: str = "{}/{}/{}"
        environments: List[str] = ['develop', 'production']
        folders: List[str] = ['css', 'images', 'js', 'robots']

        folder_keys: List[str] = []
        for environment in environments:
            for folder in folders:
                folder_keys.append(key_structure.format(
                    self._project_name,
                    environment,
                    folder
                ))

        return folder_keys

    def _generate_file(self, project_data) -> Dict[str, str]:
        """
        Creates a key/value pair of the file name and a string
        representation of an html file created by jinja.
        """
        return {}

    def create_project_directories(self) -> None:
        """
        An abstract method intended to create folders/directories for a project.
        """
        raise NotImplementedError('Trying to run compiler without a given environment')

    def create_project_files(self, project_data) -> None:
        """
        An abstract method intended to create html pages based on a json object.
        """
        raise NotImplementedError('Trying to run compiler without a given environment')
