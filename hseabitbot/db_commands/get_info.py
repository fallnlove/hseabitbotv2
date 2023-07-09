import sqlite3

from . import connect


async def get_user_list(program: str) -> [int]:
    table_query = f"""SELECT * from {program}"""
    cursor, connection = await connect.make_connection("user/sending.db")
    try:
        cursor.execute(table_query)
        content = cursor.fetchall()
    finally:
        await connect.close_connection(cursor, connection)
    return content


async def get_user_state_id(user_id: int) -> str:
    table_query = f"""SELECT state_id FROM main_table WHERE id = {user_id};"""
    cursor, connection = await connect.make_connection("user/user_id.db")
    try:
        cursor.execute(table_query)
        content = cursor.fetchall()
    finally:
        await connect.close_connection(cursor, connection)
    return content[0][0]
