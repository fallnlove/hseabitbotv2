import sqlite3

from . import connect


async def delete_user_sending(program: str, id: [str, int]) -> None:
    table_query = f"DELETE FROM {program} where id = {id}"
    cursor, connection = await connect.make_connection('user/sending.db')
    try:
        cursor.execute(table_query)
    finally:
        await connect.close_connection(cursor, connection)
