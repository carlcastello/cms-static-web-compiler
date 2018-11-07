"""
Test for the local compiler module
"""

import unittest
from unittest.mock import patch, Mock, call, mock_open
from typing import List

from app.compiler.local_compiler import LocalCompiler

# pylint: disable=missing-docstring, protected-access
class TestLocalCompiler(unittest.TestCase):

    def setUp(self) -> None:
        self._project_name: str = 'test-project-name'
        self._output_path: str = '../test-website-directory'

        self._default_compiler: LocalCompiler = LocalCompiler(self._project_name)
        self._compiler_with_path: LocalCompiler = LocalCompiler(
            self._project_name,
            output_path=self._output_path
        )

    @staticmethod
    def _expected_arguments(root_directory) -> List[type(call)]:
        return [
            call(f'{root_directory}/test-project-name/develop/css'),
            call(f'{root_directory}/test-project-name/develop/images'),
            call(f'{root_directory}/test-project-name/develop/js'),
            call(f'{root_directory}/test-project-name/develop/robots'),
            call(f'{root_directory}/test-project-name/production/css'),
            call(f'{root_directory}/test-project-name/production/images'),
            call(f'{root_directory}/test-project-name/production/js'),
            call(f'{root_directory}/test-project-name/production/robots'),
        ]

    @patch('os.path.isfile')
    @patch('os.makedirs')
    def test_create_project_directories_default_file_location(self,
                                                              mock_make_dirs: Mock,
                                                              mock_is_file: Mock) -> None:
        mock_is_file.return_value = True

        self._default_compiler.create_project_directories()

        received_arguments: List[type(call)] = mock_make_dirs.call_args_list
        expected_arguments: List[type(call)] = self._expected_arguments('../static-websites')

        self.assertEqual(expected_arguments, received_arguments)

    @patch('os.path.isfile')
    @patch('os.makedirs')
    def test_create_project_directories_with_custom_file_location(self,
                                                                  mock_make_dirs: Mock,
                                                                  mock_is_file: Mock) -> None:
        mock_is_file.return_value = True

        self._compiler_with_path.create_project_directories()

        received_arguments: List[type(call)] = mock_make_dirs.call_args_list
        expected_arguments: List[type(call)] = self._expected_arguments(self._output_path)

        self.assertEqual(expected_arguments, received_arguments)

    @patch('os.path.isdir')
    @patch('os.makedirs')
    def test_create_project_directories_with_dir_already_exist(self,
                                                               mock_make_dirs: Mock,
                                                               mock_is_dir: Mock) -> None:
        mock_is_dir.return_value = True
        self._default_compiler.create_project_directories()

        received_arguments: List[str] = mock_make_dirs.call_args_list

        self.assertEqual([], received_arguments)

    def test_save_file(self) -> None:
        mock_file: Mock = mock_open()

        file_location: str = 'file-location'
        file_content: str = 'Hello World'

        with patch('builtins.open', mock_file):
            self._compiler_with_path._save_file(file_location, file_content)

        self.assertEqual(1, mock_file.call_count)
        self.assertEqual(
            call('../test-website-directory/file-location', 'w'),
            mock_file.call_args
        )

        file_handler: Mock = mock_file().write
        self.assertEqual(1, file_handler.call_count)
        self.assertEqual(
            call(file_content),
            file_handler.call_args
        )
