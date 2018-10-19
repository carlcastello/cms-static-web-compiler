"""
Application classes and functions
"""

import os

from typing import Dict
from dotenv import load_dotenv

from app.utils import get_compiler
from app.parser import Parser
from app.parser.local_parser import LocalParser
from app.compiler import Compiler
from app.compiler.local_compiler import LocalCompiler

load_dotenv(verbose=True)

<<<<<<< HEAD
def _get_compiler(project_name: str, **kwargs: str) -> Compiler:
    return {
        'LOCAL': LocalCompiler(project_name, **kwargs)
    }.get(os.getenv('ENVIRONMENT'), Compiler(project_name))

def _get_parser(project_name: str, **kwargs: str) -> Parser:
    return {
        'LOCAL': LocalParser(project_name, **kwargs)
    }.get(os.getenv('ENVIRONMENT'), Parser(project_name, **kwargs))

def create_project_structure(project_name: str, **kwargs: str):
=======
def create_project_structure(project_name: str, **kwargs: str) -> None:
>>>>>>> SED-1
    """
    Creates the folder structure, basic html files and css

    :project_name: Name of the project/root folder
    :kwargs: Extra arguments needed for the compiler
    """
<<<<<<< HEAD

    compiler: Compiler = _get_compiler(project_name, **kwargs)
    compiler.create_project_directories()

    parser: Parser = _get_parser(project_name, **kwargs)
    project_data: dict = parser.read_project_data()


=======
    parser: Compiler = get_compiler(project_name, **kwargs)
    parser.create_project_directories()
>>>>>>> SED-1

def update_project(project_name: str) -> None:
    """
    Updates a project using an updated json object

    :project_name: Name of the project/root folder
    """
    # pylint: disable=unused-argument
    pass
