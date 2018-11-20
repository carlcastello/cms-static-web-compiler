"""
Test for the parser __init__ module
"""

import unittest
from unittest.mock import patch, Mock, mock_open, call

from typing import Dict, Any, List

from app.parser import Parser
from app.constants import MARKUP, SCSS, IMAGES

# pylint: disable=missing-docstring, protected-access
class TestParser(unittest.TestCase):

    class Template:
        # pylint: disable=too-few-public-methods
        kwargs: Dict[str, Any] = {}
        def __init__(self, mark_up: str) -> None:
            self._mark_up: str = mark_up

        def render(self, **kwargs) -> str:
            self.kwargs: Dict[str, Any] = kwargs
            return self._mark_up

    def setUp(self) -> None:
        self._parser: Parser = Parser('test-project-name')

    @patch('app.parser.Environment.get_template')
    def test__parse_markup(self,
                           mock_get_template: Mock) -> None:
        page_name: str = 'hello_world.html'
        page_content: str = 'potato salad'
        expected_page: Dict[str, str] = {
            'file_name': page_name
        }
        mark_up: str = {
            'pages': [expected_page]
        }
        template: self.Template = self.Template(page_content)
        mock_get_template.return_value = template

        returned_data: Dict[str, str] = self._parser._parse_markup(mark_up)

        self.assertEqual({page_name: page_content}, returned_data)
        self.assertEqual(expected_page, template.kwargs)

    def test_parse_sass(self) -> None:
        file_data: str = 'Oranges are not red'
        mock_file: Mock = mock_open(read_data=file_data)

        key: str = 'blues'
        value: str = 'are not purple'
        variables: Dict[str, str] = {key: value}

        other_key: str = 'Not so blue'
        other_value: str = 'say the sugarman'
        other: Dict[str, str] = {other_key: other_value}

        returned_data: Dict[str, Any] = {}
        with patch('builtins.open', mock_file):
            returned_data = self._parser._parse_scss({
                'variables': variables,
                'other': other
            })

        self.assertEqual(
            [f'{key}: {value};', file_data, f'.other{{{other_key}:{other_value};}};'],
            returned_data
        )

    def test_parse_images(self) -> None:
        file_name: str = 'Guy Fawkes'
        data: str = 'Remember Remember the fifth of november'
        images_data: str = [{'file_name': file_name, 'data': data}]

        returned_data: Dict[str, str] = self._parser._parse_images(images_data)

        self.assertEqual({file_name: data}, returned_data)


    @patch('app.parser.Parser._parse_images')
    @patch('app.parser.Parser._parse_markup')
    @patch('app.parser.Parser._parse_scss')
    def test_render_project_file(self,
                                 mock_parse_scss: Mock,
                                 mock_parse_markup: Mock,
                                 mock_parse_images: Mock) -> None:
        parsed_markup: str = 'The lion sleeps angrily.'
        parsed_scss: str = 'The quick brown fox'
        parsed_images: str = 'Obiviating the need for test'

        markup_data: Dict[str, List[Dict[str, str]]] = {'pages': [{
            'file_name': 'hello_world.html',
        }]}

        images_data: List[Dict[str, str]] = [{'file_name': 'potato.png', 'data': 'not today'}]

        scss_data: Dict[str, str] = {'variables': 'this is a css file'}

        project_data: Dict[str, Any] = {
            MARKUP: markup_data,
            IMAGES: images_data,
            SCSS: scss_data
        }

        mock_parse_markup.return_value = parsed_markup
        mock_parse_scss.return_value = parsed_scss
        mock_parse_images.return_value = parsed_images

        returned_data: Dict[str, str] = self._parser.render_project_file(project_data)

        self.assertEqual(call(markup_data), mock_parse_markup.call_args)
        self.assertEqual(call(scss_data), mock_parse_scss.call_args)
        self.assertEqual(
            {MARKUP: parsed_markup, IMAGES: parsed_images, SCSS: parsed_scss},
            returned_data
        )
