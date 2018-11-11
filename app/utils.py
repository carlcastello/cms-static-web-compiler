"""
A file containing functions to fetch environment dependent classes
"""

import os

from app.parser import Parser
from app.parser.local_parser import LocalParser
from app.compiler import Compiler
from app.compiler.local_compiler import LocalCompiler

def get_compiler(project_name: str, **kwargs: str) -> Compiler:
    """
    Returns the compiler class based on environment
    """
    compiler: Compiler = {
        'LOCAL': LocalCompiler
    }.get(os.getenv('ENVIRONMENT'))

    return compiler(project_name, **kwargs)

def get_parser(project_name: str, **kwargs: str) -> Parser:
    """
    Returns the parser class based on the environment
    """
    parser: Parser = {
        'LOCAL': LocalParser
    }.get(os.getenv('ENVIRONMENT'))

    return parser(project_name, **kwargs)
