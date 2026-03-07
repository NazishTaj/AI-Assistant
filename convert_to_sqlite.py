<<<<<<< HEAD
import mysql.connector
import sqlite3
import pandas as pd

# MySQL connection
mysql_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ecommerce"
)

# SQLite connection
sqlite_conn = sqlite3.connect("ecommerce.db")

cursor = mysql_conn.cursor()

# get all tables
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

for table in tables:
    table_name = table[0]

    # read table from MySQL
    df = pd.read_sql(f"SELECT * FROM {table_name}", mysql_conn)

    # write to SQLite
    df.to_sql(table_name, sqlite_conn, if_exists="replace", index=False)

print("Database converted successfully!")

mysql_conn.close()
=======
import mysql.connector
import sqlite3
import pandas as pd

# MySQL connection
mysql_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ecommerce"
)

# SQLite connection
sqlite_conn = sqlite3.connect("ecommerce.db")

cursor = mysql_conn.cursor()

# get all tables
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

for table in tables:
    table_name = table[0]

    # read table from MySQL
    df = pd.read_sql(f"SELECT * FROM {table_name}", mysql_conn)

    # write to SQLite
    df.to_sql(table_name, sqlite_conn, if_exists="replace", index=False)

print("Database converted successfully!")

mysql_conn.close()
>>>>>>> 7e05642f3959b3c581d2fd2943756d244a019264
sqlite_conn.close()