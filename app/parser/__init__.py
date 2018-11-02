"""
Holds Parser (file to memory) related classes, functions and constants that are
used by all environments
"""
from typing import List, Dict, Any

from jinja2 import Environment, BaseLoader, PackageLoader, Template, select_autoescape

from app.constants import MARKUP, IMAGES, CSS

class Parser:
    """
    A parser abstract class with common methods for all environments
    """
    def __init__(self, project_name: str, **kwargs: str) -> None:
        self._project_name: str = project_name
        self._kwargs: str = kwargs

    @staticmethod
    def __get_file_name(file_data: Dict[str, Any]) -> str:
        return f'{file_data["file_name"]}.{file_data["file_type"]}'

    def __parse_pages(self, markup: Dict[str, Any]) -> Dict[str, Any]:
        jinja_env: Environment = Environment(
            loader=PackageLoader('app', '../resources/templates'),
            autoescape=select_autoescape(['html'])
        )
        template: Template = jinja_env.get_template('base.html')

        pages: List[Dict[str, Any]] = markup['pages']
        if pages:
            del markup['pages']

        return {
            self.__get_file_name(page): template.render(**{**markup, **page}) for page in pages
        }

    def __parse_sass(self, project_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reads the main bootstrap file and the project css
        """
        with open('resources/scss/bootstrap.scss', 'r') as bootstrap_file:
            return [bootstrap_file.read()]
        return []

    def render_project_file(self, project_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a key/value pair of the file name and a string
        representation of a the file.
        """
        return {
            MARKUP: self.__parse_pages(project_data[MARKUP]),
            IMAGES: {},
            CSS: self.__parse_sass(project_data[CSS])
        }

    def get_project_data(self) -> Dict[str, Any]:
        """
            An abstract method to fetch project data
        """
        raise NotImplementedError('Trying to run parser without a given environment')
