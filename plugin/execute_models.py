import os
from typing import List

def create_models() -> bool:

    # Where and file
    folder_base: str = '\\apps'
    folder_url: str = f"{os.getcwd()}{folder_base}"
    folders: List[str] = os.listdir(folder_url)
    file: str = 'models.py'

    # File not include, only packeage
    for unknow in folders:
        if not os.path.isdir(f'{folder_url}//{unknow}'):
            folders.remove(unknow)

    # Amount
    length: int = len(folders)

    # Run models.py

    def execute(file) -> None:
        with open(file, 'r') as code:
            exec(code.read())

    # One by one
    for folder in range(0, length):
        for models in os.listdir(f"{folder_url}\\{folders[folder]}"):
            if models == file:
                execute(f"{folder_url}\\{folders[folder]}\\{file}")
    return True