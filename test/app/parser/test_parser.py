#pylint: disable=missing-docstring

import unittest
from unittest.mock import patch, Mock, mock_open, call

from typing import Dict, Any, List

from app.parser import Parser
from app.constants import MARKUP, SCSS, IMAGES

class TestParser(unittest.TestCase):

    class Template:
        # pylint: disable=too-few-public-methods
        kwargs: Dict[str, Any] = {}
        def __init__(self, mark_up):
            self._mark_up: str = mark_up

        def render(self, **kwargs) -> str:
            self.kwargs: Dict[str, Any] = kwargs
            return self._mark_up

    def setUp(self) -> None:
        self._parser: Parser = Parser('test-project-name')

    @patch('app.parser.Environment.get_template')
    def test__parse_markup(self,
                          mock_get_template: Mock) -> None:
        page_name: str = 'hello_world'
        page_type: str = 'html'
        page_content: str = 'potato salad'
        expected_page: Dict[str, str] = {
            'file_name': page_name,
            'file_type': page_type,
        }
        mark_up: str = {
            'pages': [expected_page]
        }
        template: self.Template = self.Template(page_content)
        mock_get_template.return_value = template

        returned_data: Dict[str, str] = self._parser._parse_markup(mark_up)

        self.assertEqual(
            {f'{page_name}.{page_type}': page_content},
            returned_data
        )
        self.assertEqual(
            expected_page,
            template.kwargs
        )

    def test_parse_sass(self) -> None:
        file_data: str = 'Oranges are not red'
        mock_file: Mock = mock_open(read_data=file_data)

        variables: str = 'Blues are not purple'

        returned_data: Dict[str, Any] = {}
        with patch('builtins.open', mock_file):
            returned_data = self._parser._parse_scss({
                'variables': variables
            })

        self.assertEqual([variables, file_data], returned_data)

    @patch('app.parser.Parser._parse_markup')
    @patch('app.parser.Parser._parse_scss')
    def test_render_project_file(self,
                                 mock_parse_scss: Mock,
                                 mock_parse_markup: Mock) -> None:
        parsed_markup = 'The lion sleeps angrily.'
        parsed_scss = 'The quick brown fox'

        markup_data: Dict[str, str] = {
            'file_name': 'hello_world',
            'file_type': 'html',
        }

        markup_data: Dict[str, List[Dict[str, str]]] = {'pages': [{
            'file_name': 'hello_world',
            'file_type': 'html',
        }]}

        scss_data = {'variables': 'this is a css file'}

        project_data: Dict[str, Any] = {
            MARKUP: markup_data,
            IMAGES: {},
            SCSS: scss_data
        }

        mock_parse_markup.return_value = parsed_markup
        mock_parse_scss.return_value = parsed_scss

        returned_data: Dict[str, str] = self._parser.render_project_file(project_data)

        self.assertEqual(call(markup_data), mock_parse_markup.call_args)
        self.assertEqual(call(scss_data), mock_parse_scss.call_args)
        self.assertEqual(
            {MARKUP: parsed_markup, IMAGES: {}, SCSS: parsed_scss},
            returned_data
        )
