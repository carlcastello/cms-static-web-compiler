import unittest

from app.compiler import Compiler

class Test_Compiler(unittest.TestCase):

    def setUp(self) -> None:
        self._compiler = Compiler('test-project-name')        

    def test_create_project_structure(self) -> None:
        expected_keys = [
            'test-project-name/develop/css',
            'test-project-name/develop/images',
            'test-project-name/develop/js',
            'test-project-name/develop/robots',
            'test-project-name/production/css',
            'test-project-name/production/images',
            'test-project-name/production/js',
            'test-project-name/production/robots',
        ]
        returned_keys = self._compiler._generate_project_keys()
        self.assertEqual(expected_keys, returned_keys)
