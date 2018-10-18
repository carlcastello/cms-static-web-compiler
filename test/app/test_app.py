# pylint: disable=missing-docstring

import unittest
from unittest.mock import patch, Mock

from app import create_project_structure
from app.compiler.local_compiler import LocalCompiler

class TestApp(unittest.TestCase):

    @patch('app.compiler.local_compiler.LocalCompiler')
    @patch('app.get_compiler')
    def test_create_project_structure(self,
                                      mock_get_compiler: Mock,
                                      mock_compiler: Mock) -> None:
        mock_get_compiler.return_value = mock_compiler

        create_project_structure('test-local-project')

        self.assertEqual(mock_compiler.create_project_directories.call_count, 1)
