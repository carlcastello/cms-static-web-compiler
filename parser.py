import json
from pathlib import Path

def read_file(path: str) -> dict:
    from pathlib import Path

    file_path = Path(path)
    if file_path.is_file():
        data = {}
        with open(path, 'r') as file:
            data = json.load(file)
        return data
    else:
        raise FileNotFoundError('File in the path of {} not found'.format(path))