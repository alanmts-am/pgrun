from database.connection import get_connnection
from model.database import Database
from model.result import Result


def run_update_query(database: Database, query: str) -> None:
    try:
        conn = get_connnection(database=database)

        cur = conn.cursor()
        cur.execute(query)

        conn.commit()
        cur.close()
        conn.close()

        print(f'Host: {database.host} - Database: {database.db_name} - OK')
    except Exception as e:
        print(f'Host: {database.host} - Database: {database.db_name} - {e}')


def run_select_query(database: Database, query: str):
    try:
        conn = get_connnection(database=database)

        cur = conn.cursor()
        cur.execute(query)

        records = cur.fetchall()
        columns = [desc[0] for desc in cur.description]

        conn.commit()
        cur.close()
        conn.close()

        print(f'Host: {database.host} - Database: {database.db_name} - OK')
        return Result(data=records, columns=columns)
    except:
        print(f'Host: {database.host} - Database: {database.db_name} - ERROR')
        return Result(data=None, columns=[])
