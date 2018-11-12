"""
Holds Parser (file to memory) related classes, functions and constants that are
used by all environments
"""
from typing import List, Dict, Any

from jinja2 import Environment, BaseLoader, PackageLoader, Template, select_autoescape

from app.constants import MARKUP, IMAGES, SCSS

class Parser:
    """
    A parser abstract class with common methods for all environments
    """
    def __init__(self, project_name: str, **kwargs: str) -> None:
        self._project_name: str = project_name
        self._kwargs: str = kwargs

    @staticmethod
    def _parse_markup(markup: Dict[str, Any]) -> Dict[str, Any]:
        """
        Parse markup and render as html
        """
        jinja_env: Environment = Environment(
            loader=PackageLoader('app', '../resources/templates'),
            autoescape=select_autoescape(['html'])
        )
        template: Template = jinja_env.get_template('base.html')

        pages: List[Dict[str, Any]] = markup['pages']
        if pages:
            del markup['pages']

        return {
            page['file_name']: template.render(**markup, **page) for page in pages
        }

    @staticmethod
    def _parse_scss(scss: Dict[str, Any]) -> str:
        """
        Parse project css and combine with the main bootstrap file
        """
        def _parse_variables() -> str:
            variables: Dict[str, str] = scss.get('variables', {})
            return ''.join([f'{key}: {value};' for key, value in variables.items()])

        with open('resources/scss/bootstrap.scss', 'r') as bootstrap_file:
            return [_parse_variables(), bootstrap_file.read()]
        return ""

    @staticmethod
    def _parse_images(images: List[Dict[str, str]]) -> Dict[str, str]:
        """
        Parse images data to {file_name: content} format
        """
        return {image['file_name']: image['data'] for image in images}


    def render_project_file(self, project_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a key/value pair of the file name and a string
        representation of a the file.
        """
        return {
            MARKUP: self._parse_markup(project_data[MARKUP]),
            IMAGES: self._parse_images(project_data[IMAGES]),
            SCSS: self._parse_scss(project_data[SCSS])
        }

    def get_project_data(self) -> Dict[str, Any]:
        """
        An abstract method to fetch project data
        """
        raise NotImplementedError
