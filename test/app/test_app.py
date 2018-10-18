# pylint: disable=missing-docstring

import unittest
from unittest.mock import patch, Mock

from app import create_project_structure

class TestApp(unittest.TestCase):

    @patch('app.compiler.local_compiler.LocalCompiler.create_project_directories')
    @patch('os.getenv')
    def test_create_project_structure(self,
                                      mock_get_env: Mock,
                                      mock_create_project_directories: Mock) -> None:
        mock_get_env.return_value = 'LOCAL'

        create_project_structure('test-local-project')

        self.assertEqual(mock_create_project_directories.call_count, 1)
