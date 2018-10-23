"""
A file containing functions to fetch environment dependent classes
"""

import os

from app.compiler import Compiler
from app.compiler.local_compiler import LocalCompiler

def get_compiler(project_name: str, **kwargs: str) -> Compiler:
    """
    Returns the compiler class based on environment
    """
    compiler: Compiler = {
        'LOCAL': LocalCompiler(project_name, **kwargs)
    }.get(os.getenv('ENVIRONMENT'), Compiler(project_name))
    return compiler
