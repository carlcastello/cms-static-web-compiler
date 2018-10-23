"""
Application classes and functions
"""

import os

from typing import Dict
from dotenv import load_dotenv

from app.utils import get_compiler
from app.compiler import Compiler
from app.compiler.local_compiler import LocalCompiler

load_dotenv(verbose=True)

def create_project_structure(project_name: str, **kwargs: str) -> None:
    """
    Creates the folder structure, basic html files and css

    :project_name: Name of the project/root folder
    :kwargs: Extra arguments needed for the compiler
    """
    parser: Compiler = get_compiler(project_name, **kwargs)
    parser.create_project_directories()

def update_project(project_name: str) -> None:
    """
    Updates a project using an updated json object

    :project_name: Name of the project/root folder
    """
    # pylint: disable=unused-argument
    pass
