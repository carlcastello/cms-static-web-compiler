import os

from dotenv import load_dotenv

from app.compiler import Compiler
from app.compiler.local_compiler import LocalCompiler

load_dotenv(verbose=True)

def _get_compiler(project_name: str, **kwargs: dict) -> Compiler:
    return {
        'LOCAL_COMPILER': LocalCompiler(project_name, **kwargs)
    }.get(os.getenv('COMPILER_ENV'), Compiler(project_name))

def create_project_structure(project_name: str, **kwargs: dict) -> None:
    parser = _get_compiler(project_name, **kwargs)
    parser.create_project_directories()

def update_project(project_name: str) -> None:
    pass
