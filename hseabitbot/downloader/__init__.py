from .download import bachelor_programs
from .download import file_hashes


def __init__() -> None:
    for program in bachelor_programs:
        file_hashes[program] = ''
