from typing import List
from io import StringIO
import time
from datetime import timedelta
import yaml
from pathlib import Path
from prettytable import PrettyTable
import pandas as pd

from model.database import Database
from model.result import Result

from database.query import run_select_query, run_update_query


def return_select_result(databases: List[Database], query: str, file_name: str = 'data'):
    table = PrettyTable()
    for database in databases:
        try:
            result: Result = run_select_query(database=database, query=query)

            table.field_names = result.columns
            table.add_rows(result.data)

            aps_json = pd.read_json(
                StringIO(table.get_json_string(header=False)))
            aps_json.to_excel(file_name + '.xlsx',
                              columns=table.field_names)
        except Exception as e:
            print(e)


def return_update_query(databases: List[Database], query: str):
    initial_time = time.time()
    for database in databases:
        print(" ")
        print("==================================")
        print(f"Iniciando em {database.db_name}")
        database_initial_time = time.time()
        run_update_query(database=database, query=query)
        database_final_time = time.time()

        database_duration = database_final_time - database_initial_time
        time_database_duration = timedelta(seconds=database_duration)
        print(f"Tempo: {time_database_duration}")
    final_time = time.time()

    duration = final_time - initial_time
    time_duration = timedelta(seconds=duration)

    print(" ")
    print("==================================")
    print(f"Tempo total: {time_duration}")
    print("==================================")


def organize_databases(main_database: Database, main_query: str) -> List[Database]:
    databases: List[Database] = []

    raw_databases: Result = run_select_query(
        main_database, query=main_query)

    for database in raw_databases.data:
        databases.append(
            Database(host=database[0], port=database[1], db_name=database[2], username=database[3], pwd=database[4]))

    return databases

CONFIG_PATH = "config.yml"
CONFIG_LOCAL_PATH = "config.local.yml"
QUERY_PATH = "query.sql"

if(Path(CONFIG_LOCAL_PATH).exists()):
    with open(CONFIG_LOCAL_PATH, "r", encoding='utf8') as file:
        config = yaml.full_load(file)
else:
    with open(CONFIG_PATH, "r", encoding='utf8') as file:
        config = yaml.full_load(file)

with open(QUERY_PATH, "r", encoding='utf8') as file:
    query = file.read()

HOST = config["connection"]["host"]
PORT = config["connection"]["port"]
DB_NAME = config["connection"]["database"]
USER = config["connection"]["username"]
PASSWORD = config["connection"]["password"]

DATABASE_QUERY = config["sql"]["database"]

IS_SELECT = config["options"]["select"]

databases: List[Database] = organize_databases(
    main_database=Database(host=HOST, port=PORT, db_name=DB_NAME, username=USER, pwd=PASSWORD), main_query=DATABASE_QUERY)

if IS_SELECT:
    return_select_result(databases=databases, query=query)
else:
    return_update_query(databases=databases, query=query)
