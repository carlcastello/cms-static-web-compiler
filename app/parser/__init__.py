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
    def render_project_file(project_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a key/value pair of the file name and a string
        representation of a the file.
        """
        def _get_file_name(file_data: Dict[str, Any]) -> str:
            return file_data['file_name'] + '.' + file_data['file_type']

        def _render_pages() -> Dict[str, Any]:
            jinja_env: Environment = Environment(
                loader=PackageLoader('app', 'templates'),
                autoescape=select_autoescape(['html'])
            )
            template: Template = jinja_env.get_template('base.html')

            markup: Dict[str, Any] = project_data.get(MARKUP, {})
            pages: List[Dict[str, Any]] = markup.get('pages', [])
            if pages:
                del markup['pages']

            return {
                _get_file_name(page): template.render(**{**markup, **page}) for page in pages
            }

        return {
            MARKUP: _render_pages(),
            IMAGES: {},
            CSS: {}
        }

    def get_project_data(self) -> Dict[str, Any]:
        """
            An abstract method to fetch project data
        """
        raise NotImplementedError('Trying to run parser without a given environment')
