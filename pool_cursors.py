from connection_pool import Connection


class Cursors:
    def __init__(self):
        self._connection = None
        self._cursor = None

    @classmethod
    def create_cursor(cls):
        cls._connection = Connection.get_connection()
        cls._cursor = cls._connection.cursor()
        return cls._cursor

    @classmethod
    def close_cursor(cls):
        cls._cursor.close()
        Connection.leave_connection(cls._connection)
