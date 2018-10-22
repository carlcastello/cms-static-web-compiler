"""
Application classes and functions
"""

import os

from typing import Dict, Any
from dotenv import load_dotenv

from app.utils import get_compiler, get_parser
from app.parser import Parser
from app.parser.local_parser import LocalParser
from app.compiler import Compiler
from app.compiler.local_compiler import LocalCompiler

load_dotenv(verbose=True)


def create_project_structure(project_name: str, **kwargs: str) -> None:
    """
    Creates the folder structure, basic html files and css

    :project_name: Name of the project/root folder
    :kwargs: Extra arguments needed for the compiler
    """
    parser: Parser = get_parser(project_name, **kwargs)
    compiler: Compiler = get_compiler(project_name, **kwargs)

    compiler.create_project_directories()
    project_data: Dict[str, Any] = parser.get_project_data()
    project_file: Dict[str, Any] = parser.render_project_file(project_data)
    compiler.create_project_files  (project_file)

def update_project(project_name: str) -> None:
    """
    Updates a project using an updated json object

    :project_name: Name of the project/root folder
    """
    # pylint: disable=unused-argument
    pass
