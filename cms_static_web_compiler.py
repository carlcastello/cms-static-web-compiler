import os
import sys

from dotenv import load_dotenv

from parser import Parser
from parser.local_parser import LocalParser

load_dotenv(verbose=True)

def get_parser(project_name: str, **kwargs: dict) -> Parser:
    return {
        'LOCAL_PARSER': LocalParser(project_name, **kwargs)
    }[os.getenv('PARSER_ENV')]

def create_project_structure(project_name: str, **kwargs: dict) -> None:
    parser = get_parser(project_name, **kwargs)
    parser.create_project_directories()

def update_project(project_name: str) -> None:
    pass


if __name__ == '__main__':
    from argparse import ArgumentParser
    terminal_parser = ArgumentParser()
    
    terminal_parser.add_argument('--name', help='The project file name', type=str)
    terminal_parser.add_argument('--output_path', help='The project file name', type=str)
    
    terminal_arguments = terminal_parser.parse_args()

    create_project_structure(terminal_arguments.name)