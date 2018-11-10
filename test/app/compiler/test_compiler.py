"""
Test for the compiler __init__ module
"""

import unittest
from unittest.mock import Mock, patch, call

from typing import Dict, Any, List

from app.constants import MARKUP, SCSS
from app.compiler import Compiler

# pylint: disable=missing-docstring, protected-access
class TestCompiler(unittest.TestCase):

    def setUp(self) -> None:
        self._project_name: str = 'test-project-name'
        self._compiler: Compiler = Compiler(self._project_name)

    def test__generate_project_keys(self) -> None:
        # pylint: disable=protected-access
        expected_keys = [
            f'{self._project_name}/develop/css',
            f'{self._project_name}/develop/images',
            f'{self._project_name}/develop/js',
            f'{self._project_name}/develop/robots',
            f'{self._project_name}/production/css',
            f'{self._project_name}/production/images',
            f'{self._project_name}/production/js',
            f'{self._project_name}/production/robots ',
        ]
        returned_keys = self._compiler._generate_project_keys()
        self.assertEqual(expected_keys, returned_keys)

    @patch('app.compiler.Compiler._save_file')
    def test__compile_markup(self,
                             mock_save_file: Mock) -> None:
        environment: str = 'development'
        file_name: str = 'file_name.html'
        files: Dict[str, Any] = {file_name: 'Hello world'}

        self._compiler._compile_markup(environment, files)

        self.assertEqual(1, mock_save_file.call_count)
        self.assertEqual(
            call(f'{self._project_name}/{environment}/{file_name}', files[file_name]),
            mock_save_file.call_args
        )

    @patch('app.compiler.sass_compile')
    @patch('app.compiler.Compiler._save_file')
    def test__compile_css(self,
                          mock_save_file: Mock,
                          mock_sass_compile: Mock) -> None:
        environment: str = 'development'
        files: List[str] = ['Hello', 'World']
        compiled_files: str = 'ThisIsACompiledCss'

        mock_sass_compile.return_value = compiled_files

        self._compiler._compile_scss(environment, files)

        self.assertEqual(1, mock_sass_compile.call_count)
        self.assertEqual(1, mock_save_file.call_count)

        self.assertEqual(
            call(string=(''.join(files)),
                 include_paths=('resources/scss',),
                 output_style='compressed'),
            mock_sass_compile.call_args
        )
        self.assertEqual(
            call(f'{self._project_name}/{environment}/css/main.css', compiled_files),
            mock_save_file.call_args
        )

    @patch('app.compiler.Compiler._compile_scss')
    @patch('app.compiler.Compiler._compile_markup')
    def test_create_project_files_compile_markup_files(self,
                                                       mock_compile_markup: Mock,
                                                       mock_compile_css: Mock) -> None:
        file_name: str = 'file_name.html'
        file_content: str = 'Hello World'

        project_files: Dict[str, Dict[str, str]] = {
            MARKUP: {file_name: file_content},
            SCSS: ['Hello', 'World']
        }

        self._compiler.create_project_files(project_files)

        self.assertEqual(2, mock_compile_css.call_count)
        self.assertEqual(
            [call('develop', project_files[SCSS]), call('production', project_files[SCSS])],
            mock_compile_css.call_args_list
        )

        self.assertEqual(2, mock_compile_css.call_count)
        self.assertEqual(
            [call('develop', project_files[MARKUP]), call('production', project_files[MARKUP])],
            mock_compile_markup.call_args_list
        )
