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
