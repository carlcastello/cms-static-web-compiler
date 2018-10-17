
class Parser:

    def __init__(self, project_name: str, **kwargs: str) -> None:
        self._project_name = project_name

    def read_project_data(self):
        """
            An abstract method to fetch project data
        """
        raise NotImplementedError('Trying to run parser without a given environment')