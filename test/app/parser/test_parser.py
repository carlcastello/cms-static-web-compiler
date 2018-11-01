#pylint: disable=missing-docstring

import unittest
from unittest.mock import patch, Mock, mock_open

from typing import Dict, Any

from app.parser import Parser
from app.constants import MARKUP, CSS, IMAGES

class TestParser(unittest.TestCase):

    class Template:
        # pylint: disable=too-few-public-methods
        kwargs = {}
        def __init__(self, mark_up):
            self._mark_up: str = mark_up

        def render(self, **kwargs) -> str:
            self.kwargs: Dict[str, Any] = kwargs
            return self._mark_up

    def setUp(self) -> None:
        self._parser = Parser('test-project-name')

    @patch('app.parser.Environment.get_template')
    def test_render_project_file(self,
                                 mock_get_template: Mock) -> None:

        file_name: str = 'potato_salad'
        file_type: str = 'html'
        mark_up: str = 'Hello World!'
        file_data = 'Oranges are not red'

        template = self.Template(mark_up)
        mock_get_template.return_value = template
        mock_file: Mock = mock_open(read_data=file_data)

        page_one: Dict[str, str] = {
            'file_name': file_name,
            'file_type': file_type
        }

        project_data: Dict[str, Any] = {
            MARKUP: {'pages': [page_one]},
            IMAGES: {}
            CSS: []
        }

        returned_data: Dict[str, Any] = {}
        with patch('builtins.open', mock_file):
            returned_data = self._parser.render_project_file(project_data)

        self.assertEqual(
            returned_data,
            {MARKUP: {f'{file_name}.{file_type}': f'{mark_up}'},
             Ima: {},
             CSS: [file_data]}
        )
        self.assertEqual(template.kwargs, page_one)
