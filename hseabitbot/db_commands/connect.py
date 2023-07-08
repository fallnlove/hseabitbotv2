import sqlite3


async def make_connection(path: str) -> (sqlite3.Cursor, sqlite3.connect):
    sqlite_connection = sqlite3.connect(path)
    return sqlite_connection.cursor(), sqlite_connection


async def close_connection(cur: sqlite3.Cursor, conn: sqlite3.connect) -> None:
    cur.close()
    conn.commit()
    conn.close()
