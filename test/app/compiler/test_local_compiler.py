# pylint: disable=missing-docstring

import unittest
from unittest.mock import patch, Mock, call
from typing import List

from app.compiler.local_compiler import LocalCompiler

class TestLocalCompiler(unittest.TestCase):

    def setUp(self) -> None:
        self._default_compiler = LocalCompiler('test-project-name')

    @staticmethod
    def _expected_arguments(root_directory) -> List[call]:
        return [
            call('{}test-project-name/develop/css'.format(root_directory)),
            call('{}test-project-name/develop/images'.format(root_directory)),
            call('{}test-project-name/develop/js'.format(root_directory)),
            call('{}test-project-name/develop/robots'.format(root_directory)),
            call('{}test-project-name/production/css'.format(root_directory)),
            call('{}test-project-name/production/images'.format(root_directory)),
            call('{}test-project-name/production/js'.format(root_directory)),
            call('{}test-project-name/production/robots'.format(root_directory)),
        ]

    @patch('os.path.isfile')
    @patch('os.makedirs')
    def test_create_project_directories_default_file_location(self,
                                                              mock_make_dirs: Mock,
                                                              mock_is_file: Mock) -> None:
        mock_is_file.return_value = True

        self._default_compiler.create_project_directories()

        received_arguments = mock_make_dirs.call_args_list
        expected_arguments = self._expected_arguments('../static-websites/')

        self.assertEqual(received_arguments, expected_arguments)

    @patch('os.path.isfile')
    @patch('os.makedirs')
    def test_create_project_directories_with_custom_file_location(self,
                                                                  mock_make_dirs: Mock,
                                                                  mock_is_file: Mock) -> None:
        mock_is_file.return_value = True

        compiler = LocalCompiler('test-project-name', output_path='../test-website-directory/')
        compiler.create_project_directories()

        received_arguments = mock_make_dirs.call_args_list
        expected_arguments = self._expected_arguments('../test-website-directory/')

        self.assertEqual(received_arguments, expected_arguments)

    @patch('os.path.isfile')
    @patch('os.makedirs')
    def test_create_project_directories_with_file_already_exist(self,
                                                                mock_make_dirs: Mock,
                                                                mock_is_file: Mock) -> None:
        mock_is_file.return_value = False
        compiler = LocalCompiler('test-project-name')
        compiler.create_project_directories()

        received_arguments = mock_make_dirs.call_args_list

        self.assertEqual(received_arguments, [])
