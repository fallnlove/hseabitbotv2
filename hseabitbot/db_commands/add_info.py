import sqlite3

from . import connect


program_id = {}


async def add_user_sending(program: str, id: [str, int]) -> None:
    table_query = f"INSERT INTO {program_id[program]} (id)  VALUES  ({id})"
    cursor, connection = await connect.make_connection('hseabitbot/user/sending.db')
    try:
        cursor.execute(table_query)
    finally:
        await connect.close_connection(cursor, connection)


async def add_user_id(id: int, state_id: str) -> None:
    table_query = f"INSERT INTO main_table (id, state_id)  VALUES  ({id}, '{state_id}')"
    cursor, connection = await connect.make_connection('hseabitbot/user/user_id.db')
    try:
        cursor.execute(table_query)
    finally:
        await connect.close_connection(cursor, connection)



async def change_user_id(id: int, state_id: str) -> None:
    table_query = f"UPDATE main_table SET state_id = '{state_id}' WHERE id = {id}"
    cursor, connection = await connect.make_connection('hseabitbot/user/user_id.db')
    try:
        cursor.execute(table_query)
    finally:
        await connect.close_connection(cursor, connection)
