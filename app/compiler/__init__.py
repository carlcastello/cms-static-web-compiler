from typing import List

class Compiler:

    def __init__(self, project_name: str) -> None:
        self._project_name = project_name

    def generate_project_keys(self) -> List:
        key_structure = "{}/{}/{}"
        environments = ['develop', 'production']
        folders = ['css', 'images', 'js']
        
        folder_keys = []
        for environment in environments:
            for folder in folders:
                folder_keys.append(key_structure.format(self._project_name, environment, folder))

        return folder_keys


    def create_project_directories(self) -> None:
        raise NotImplementedError
