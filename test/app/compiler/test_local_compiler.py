# pylint: disable=missing-docstring

import unittest
from unittest.mock import patch, Mock, call, mock_open
from typing import List, Dict, Any

from app.constants import MARKUP
from app.compiler.local_compiler import LocalCompiler

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
            call('{}/test-project-name/develop/css'.format(root_directory)),
            call('{}/test-project-name/develop/images'.format(root_directory)),
            call('{}/test-project-name/develop/js'.format(root_directory)),
            call('{}/test-project-name/develop/robots'.format(root_directory)),
            call('{}/test-project-name/production/css'.format(root_directory)),
            call('{}/test-project-name/production/images'.format(root_directory)),
            call('{}/test-project-name/production/js'.format(root_directory)),
            call('{}/test-project-name/production/robots'.format(root_directory)),
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

        self.assertEqual(received_arguments, expected_arguments)

    @patch('os.path.isfile')
    @patch('os.makedirs')
    def test_create_project_directories_with_custom_file_location(self,
                                                                  mock_make_dirs: Mock,
                                                                  mock_is_file: Mock) -> None:
        mock_is_file.return_value = True

        self._compiler_with_path.create_project_directories()

        received_arguments: List[type(call)] = mock_make_dirs.call_args_list
        expected_arguments: List[type(call)] = self._expected_arguments(self._output_path)

        self.assertEqual(received_arguments, expected_arguments)

    @patch('os.path.isdir')
    @patch('os.makedirs')
    def test_create_project_directories_with_dir_already_exist(self,
                                                               mock_make_dirs: Mock,
                                                               mock_is_dir: Mock) -> None:
        mock_is_dir.return_value = True
        self._default_compiler.create_project_directories()

        received_arguments: List[str] = mock_make_dirs.call_args_list

        self.assertEqual(received_arguments, [])

    def test_create_project_files_compile_markup_files(self) -> None:
        mock_file: Mock = mock_open()
        project_files: Dict[str, Any] = {MARKUP: {'file_name.html': 'Hello World'}}

        with patch('builtins.open', mock_file):
            self._compiler_with_path.create_project_files(project_files)

        file_path = '{}/{}/{}/file_name.html'.format(self._output_path, self._project_name, {})
        self.assertEqual(mock_file.call_count, 2)
        self.assertEqual(
            mock_file.call_args_list,
            [call(file_path.format('develop'), 'w'), call(file_path.format('production'), 'w')]
        )

        file_handler = mock_file().write
        self.assertEqual(file_handler.call_count, 2)
        self.assertEqual(file_handler.call_args_list, [call('Hello World'), call('Hello World')])
