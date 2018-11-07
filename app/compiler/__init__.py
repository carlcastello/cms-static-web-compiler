"""
Holds Compiler (memory to file) related classes, functions and constants that are
used by all environments
"""

from typing import List, Dict, Any

from sass import compile as sass_compile

from app.constants import MARKUP, IMAGES, SCSS, JS, ROBOTS

class Compiler:
    """
    A compiler abstract class with common methods for all environments
    """

    _environments: List[str] = ['develop', 'production']
    _folders: List[str] = ['css', IMAGES, JS, ROBOTS]

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
                folder_keys.append(f'{self._project_name}/{environment}/{folder}')

        return folder_keys

    def create_project_directories(self) -> None:
        """
        An abstract method intended to create folders/directories for a project.
        """
        raise NotImplementedError


    def _save_file(self, file_location: str, file_content: str) -> None:
        """
        A abstract method to save a file that differs with implementation
        """
        raise NotImplementedError

    def _compile_markup(self, environment: str, files: Dict[str, Any]) -> None:
        for file_name, file_content in files.items():
            file_location: str = f'{self._project_name}/{environment}/{file_name}'
            self._save_file(file_location, file_content)

    def _compile_scss(self, environment: str, files: List[str]) -> None:
        file_content: str = sass_compile(
            string=(''.join(files)),
            include_paths=('resources/scss',),
            output_style='compressed'
        )
        file_location: str = f'{self._project_name}/{environment}/css/main.css'
        self._save_file(file_location, file_content)


    def create_project_files(self, project_files: Dict[str, Any]) -> None:
        """
        A method responsible for creating project files. e.i. html markups and css
        """
        for environment in self._environments:
            for file_category, files in project_files.items():
                if file_category == MARKUP:
                    self._compile_markup(environment, files)
                elif file_category == SCSS:
                    self._compile_scss(environment, files)
