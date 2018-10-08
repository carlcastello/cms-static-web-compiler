import os
import sys

from app import create_project_structure
from app.compiler import Compiler
from app.compiler.local_compiler import LocalCompiler


if __name__ == '__main__':
    from argparse import ArgumentParser
    terminal_parser = ArgumentParser()
    
    terminal_parser.add_argument('--name', help='The project file name', type=str)
    terminal_parser.add_argument('--output_path', help='The project file name', type=str)
    
    terminal_arguments = terminal_parser.parse_args()

    create_project_structure(terminal_arguments.name)