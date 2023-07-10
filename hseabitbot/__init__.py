from hseabitbot import downloader
from hseabitbot import parser
from hseabitbot.db_commands import add_info
from hseabitbot.utils import config


def __init__() -> None:
    downloader.__init__(config.bachelor_programs)
    for prog, prog_id in zip(config.program_names, config.bachelor_programs):
        add_info.program_id[prog] = prog_id
