# pylint: disable=missing-docstring

import unittest
from unittest.mock import patch, Mock

from typing import Dict, Any

from app.parser import Parser
from app.constants import MARKUP

class TestParser(unittest.TestCase):

    def setUp(self) -> None:
        self._parser = Parser('test-project-name')

    @patch('app.parser.Environment.get_template')
    def test_render_project_file(self,
                                 mock_get_template: Mock) -> None:

        file_name: str = 'potato_salad'
        file_type: str = 'html'
        mark_up: str = 'Hello World!'

        class Template:
            def render(self, **kwargs):
                self.kwargs: Dict[str, Any]= kwargs
                return mark_up

        template = Template()
        mock_get_template.return_value = template

        page_one: Dict[str, str] = {
            'name': file_name,
            'file_type': file_type
        }
        project_data: Dict[str, Any] = {
            MARKUP: {'pages': [page_one]}
        }
        returned_data: Dict[str, Any] = self._parser.render_project_file(project_data)
        self.assertEqual(
            {MARKUP: {f'{file_name}.{file_type}': f'{mark_up}'}, 'images': {}, 'css': {}},
            returned_data
        )
        self.assertEqual(page_one, template.kwargs)