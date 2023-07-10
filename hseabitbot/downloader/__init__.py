from utils import config
from .download import file_hashes


def __init__() -> None:
    for program in config.bachelor_programs:
        file_hashes[program] = ''
