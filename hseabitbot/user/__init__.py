import sqlite3
import sys

sys.path.append("../")

from utils import config

bachelor_programs = config.bachelor_programs


def __init__():
    connection = sqlite3.connect('user_id.db')
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE main_table (
     id INTEGER PRIMARY KEY,
     state_id TEXT NOT NULL
    );""")
    cursor.close()
    connection.close()

    connection = sqlite3.connect('sending.db')
    cursor = connection.cursor()
    for program in bachelor_programs:
        cursor.execute(f"""CREATE TABLE {program} (
             id INTEGER PRIMARY KEY
            );""")
    cursor.close()
    connection.close()


__init__()
