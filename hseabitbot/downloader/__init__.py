from .download import file_hashes


def __init__(bachelor_programs: [str]) -> None:
    for program in bachelor_programs:
        file_hashes[program] = ''
