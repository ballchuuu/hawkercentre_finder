import sqlite3

from app.core.sqlite.client import Sqlite3

def test_db_sqlite_client():
    test_client = Sqlite3()
    assert type(test_client.cur) == sqlite3.Cursor

    # check if get_distance function exists
    query = """
    SELECT EXISTS
        (SELECT 1
            FROM PRAGMA_FUNCTION_LIST
        WHERE name = 'get_distance');
    """

    test_client.cur.execute(query)
    result = test_client.cur.fetchone()
    assert result == (1,)

    # close conn
    test_client.conn.close()
