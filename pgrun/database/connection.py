import psycopg2
from model.database import Database


def get_connnection(database: Database):
    return psycopg2.connect(**{
        "host": database.host,
        "port": database.port,
        "database": database.db_name,
        "user": database.username,
        "password": database.pwd
    })
