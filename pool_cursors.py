from connection_pool import Connection


class Cursors:
    def __init__(self):
        self._connection = None
        self._cursor = None

    def __enter__(self):
        self._connection = Connection().get_connection()
        self._cursor = self._connection.cursor()
        return self._cursor

    def __exit__(self, exception_kind, exception_value, exception_detail):
        if exception_value:
            self._connection.rollback()
        else:
            self._connection.commit()

        self._cursor.close()
        Connection().leave_connection(self._connection)
