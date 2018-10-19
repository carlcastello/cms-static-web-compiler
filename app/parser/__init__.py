"""
Holds Parser (inputs to json) related classes, functions and constants that are
used by all environments
"""


class Parser:
    """
    A parser abstract class with common methods for all environments
    """

    def __init__(self, project_name: str, **kwargs: str) -> None:
        self._project_name = project_name

    def get_project_data(self):
        """
            An abstract method to fetch project data
        """
        raise NotImplementedError('Trying to run parser without a given environment')