"""
Test for the local compiler module
"""

import unittest
from unittest.mock import Mock, call, patch, mock_open
from json import dumps

from typing import Dict

from app.parser.local_parser import LocalParser

# pylint: disable=missing-docstring
class TestLocalParser(unittest.TestCase):

    _project_name: str = 'test-project-name'

    def setUp(self) -> None:
        self._parser: LocalParser = LocalParser(self._project_name)

    def test_get_project_data(self) -> None:
        file_data: Dict[str, str] = {'hello': 'world'}
        mock_file: Mock = mock_open(read_data=dumps(file_data))

        with patch('builtins.open', mock_file):
            returned_data: Dict[str, str] = self._parser.get_project_data()
            self.assertEqual(returned_data, file_data)

        self.assertEqual(
            mock_file.call_args,
            call(f'../json-websites/{self._project_name}.json')
        )
