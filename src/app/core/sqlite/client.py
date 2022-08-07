import sqlite3

from app.core.config import settings
from app.core.sqlite.utils import get_distance

class Sqlite3:
    def __init__(self):
        self.conn = sqlite3.connect(settings.database_name)
        self.cur = self.conn.cursor()

        # create function
        self.conn.create_function("get_distance", 5, get_distance)

sqlite3 = Sqlite3()