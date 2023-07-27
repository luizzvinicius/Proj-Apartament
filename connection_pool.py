import psycopg2
from psycopg2 import pool
import dotenv

dotenv.load_dotenv(verbose=True, override=True)


class Connection:
    __host = dotenv.get_key(".env", "host")
    __password = dotenv.get_key(".env", "password")
    __user = dotenv.get_key(".env", "user")
    __port = dotenv.get_key(".env", "port")
    __db_name = dotenv.get_key(".env", "db_name")
    __min_conn = 0
    __max_conn = 3
    _pool = None

    @classmethod
    def get_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls.__min_conn, cls.__max_conn,
                    database=cls.__db_name,
                    user=cls.__user,
                    password=cls.__password,
                    host=cls.__host,
                    port=cls.__port
                )
                return cls._pool
            except psycopg2.Error as erro:
                print(f"Falha ao criar o pools de conexão: {erro}")
        else:
            return cls._pool

    @classmethod
    def get_connection(cls):
        return cls.get_pool().getconn()

    @classmethod
    def leave_connection(cls, connection):
        return cls.get_pool().putconn(connection)

    @classmethod
    def close_conn(cls):
        return cls.get_pool().closeall()
