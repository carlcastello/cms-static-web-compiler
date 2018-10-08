import os

from dotenv import load_dotenv

from app.compiler import Compiler
from app.compiler.local_compiler import LocalCompiler

load_dotenv(verbose=True)

def get_parser(project_name: str, **kwargs: dict) -> Compiler:
    return {
        'LOCAL_PARSER': LocalCompiler(project_name, **kwargs)
    }[os.getenv('PARSER_ENV')]

def create_project_structure(project_name: str, **kwargs: dict) -> None:
    parser = get_parser(project_name, **kwargs)
    parser.create_project_directories()

def update_project(project_name: str) -> None:
    pass
