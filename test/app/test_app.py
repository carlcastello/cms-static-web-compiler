# pylint: disable=missing-docstring

import unittest
from unittest.mock import patch, Mock

from app import create_project_structure

class TestApp(unittest.TestCase):

    @patch('app.compiler.local_compiler.LocalCompiler')
    @patch('app.get_parser')
    @patch('app.compiler.local_compiler.LocalCompiler')
    @patch('app.get_compiler')
    def test_create_project_structure(self,
                                      mock_get_compiler: Mock,
                                      mock_compiler: Mock,
                                      mock_get_parser: Mock,
                                      mock_parser: Mock) -> None:
        mock_get_compiler.return_value = mock_compiler
        mock_get_parser.return_value = mock_parser

        create_project_structure('test-local-project')

        self.assertEqual(mock_compiler.create_project_directories.call_count, 1)
        self.assertEqual(mock_parser.get_project_data.call_count, 1)
        self.assertEqual(mock_parser.render_project_file.call_count, 1)
        self.assertEqual(mock_compiler.create_project_files.call_count, 1)
