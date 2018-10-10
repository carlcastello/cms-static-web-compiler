"""
    Holds Compiler related classes, functions and constants that are
    used by all environments
"""

from typing import List

class Compiler:
    """
        A compiler abstract class with common methods for different environments
    """
    # pylint: disable=too-few-public-methods

    def __init__(self, project_name: str) -> None:
        """
            :project_name: Name of the project/root folder
        """
        self._project_name = project_name

    def _generate_project_keys(self) -> List[str]:
        key_structure = "{}/{}/{}"
        environments = ['develop', 'production']
        folders = ['css', 'images', 'js', 'robots']

        folder_keys = []
        for environment in environments:
            for folder in folders:
                folder_keys.append(key_structure.format(
                    self._project_name,
                    environment,
                    folder
                ))

        return folder_keys

    def create_project_directories(self) -> None:
        """
            An abstract method intended to create folders/directories for a project
        """
        raise NotImplementedError('Trying to run compiler without a given environment')
