import sys
from typing import Any

from connection import create_connection
from create_table import create_all_tables
from insert_data import insert_random_data


def format_query(table: str, key: str | None = None, value: Any | None = None):
    BASE_QUERY = f"SELECT * FROM {table} "
    CONDITION = ""
    if key is not None:
        CONDITION = f"WHERE {key}={value}"
    return BASE_QUERY + CONDITION + ";"


def perform_query(table: str, key: str | None = None, value: Any | None = None):
    query_str = format_query(table=table, key=key, value=value)

    with create_connection() as conn:
        if conn is not None:
            cur = conn.cursor()
            cur.execute(query_str)
            result = cur.fetchall()
            cur.close()
        else:
            print("Error: can't create the database connection")
    return result


def execute_queries_from_file(conn, file_path):
    with open(file_path, 'r') as file:
        queries = file.read().split(';')
        cursor = conn.cursor()
        for query in queries:
            if query.strip():
                cursor.execute(query)
                result = cursor.fetchall()
                if result is not None:
                    for row in result:
                        print(row)
        cursor.close()




def is_table_empty(conn, table):
    with conn.cursor() as cur:
        cur.execute(f"SELECT COUNT(*) FROM {table};")
        count = cur.fetchone()[0]
        return count == 0


with create_connection() as conn:
    create_all_tables(conn)

    if is_table_empty(conn, 'Students') \
            and is_table_empty(conn, 'Groups') \
            and is_table_empty(conn, 'Professors') \
            and is_table_empty(conn, 'Subjects'):
        insert_random_data(conn)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 select.py <query_file>")
    else:
        query_file = sys.argv[1]
        with create_connection() as conn:
            execute_queries_from_file(conn, query_file)

