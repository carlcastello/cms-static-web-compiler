"""
    Cms static web compiler is a python program that reads a json file
    and converts it to a bootstrap website.
"""
from typing import Dict

from app import create_project_structure, hi


def cms_static_web_compiler():
    """
        Start the project/lamda
    """
    from argparse import ArgumentParser
    terminal_parser = ArgumentParser()

    terminal_parser.add_argument('--name', help='The project file name', type=str)
    terminal_parser.add_argument('--output_path', help='The project file name', type=str)

    terminal_arguments: Dict[str, str] = terminal_parser.parse_args()

    create_project_structure(terminal_arguments.name)

if __name__ == '__main__':
    cms_static_web_compiler()
