import sqlite3

def get_schema():

    conn = sqlite3.connect("ecommerce.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    schema = ""

    for table in tables:
        table_name = table[0]

        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()

        column_names = [col[1] for col in columns]

        schema += f"\n{table_name}({', '.join(column_names)})"

    conn.close()

    return schema


def run_query(query):

    conn = sqlite3.connect("ecommerce.db")
    cursor = conn.cursor()

    try:
        cursor.execute(query)

        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]

    except Exception as e:

        rows = [(str(e),)]
        columns = ["SQL Error"]

    conn.close()

    return rows, columns