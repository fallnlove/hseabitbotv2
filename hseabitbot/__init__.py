import downloader
import parser

from db_commands import add_info
from utils import config


def __init__() -> None:
    downloader.__init__()
    for prog, prog_id in zip(config.program_names, config.bachelor_programs):
        add_info.program_id[prog] = prog_id
