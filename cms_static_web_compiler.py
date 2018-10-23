"""
Cms static web compiler is a python program that reads a json file
and converts it to a bootstrap website.
"""

from app import create_project_structure


def cms_static_web_compiler() -> None:
    """
    Start of the project
    """

    class ArgParser:
        """
        ArgParse type
        """
        # pylint: disable=too-few-public-methods

        name: str = ''
        output_path: str = ''

    from argparse import ArgumentParser
    terminal_parser: ArgumentParser = ArgumentParser()

    terminal_parser.add_argument('--name', help='The project file name', type=str, required=True)
    terminal_parser.add_argument('--output_path', help='The project file name', type=str)

    terminal_arguments: ArgParser = terminal_parser.parse_args()

    create_project_structure(terminal_arguments.name)

if __name__ == '__main__':
    cms_static_web_compiler()
