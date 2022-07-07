# database interactions

import sqlite3
import bean_table

# database queries as variables so they can be edited later
import Trigger

CREATE_REVIEWS_TABLE = """
CREATE TABLE IF NOT EXISTS reviews (id INTEGER PRIMARY KEY, name TEXT, method TEXT, rating INTEGER);"""

INSERT_BEAN = "INSERT INTO reviews (name, method, rating) VALUES (?, ?, ?);"

GET_ALL_BEANS = "SELECT * FROM reviews;"

GET_BEANS_BY_NAME = "SELECT * FROM reviews WHERE name = ? ORDER BY rating DESC;"

GET_BEST_METHOD = """
SELECT * FROM reviews 
WHERE name = ?
ORDER BY rating DESC
LIMIT 1;"""

LOWERCASE_DATABASE = """
UPDATE reviews
SET name = LOWER(name), method = lower(method);"""

# functions to call the SQL queries


def connect():
    return sqlite3.connect("data.db")


def create_table(connection, table):
    with connection:
        connection.execute(table)


def add_bean(connection, name, method, rating):
    with connection:
        connection.execute(INSERT_BEAN, (name, method, rating))
        connection.execute(bean_table.new_bean_trigger(connection, name))


def get_all_beans(connection):
    with connection:
        return connection.execute(GET_ALL_BEANS).fetchall()


def get_beans_by_name(connection, name):
    with connection:
        # (name, blank) because has to be a tuple
        return connection.execute(GET_BEANS_BY_NAME, (name,)).fetchall()


def get_best_method(connection, name):
    with connection:
        return connection.execute(GET_BEST_METHOD, (name,)).fetchone()


# created to make my prevously open text entries uniformly lowercase for GROUP BY funcitonality
def lowercase_database():
    connection = connect()
    with connection:
        connection.execute(LOWERCASE_DATABASE)


# only needed to be ran once on older data that had been added before inputs were formatted to lower
# lowercase_database()
connection = connect()
print(connection.execute("SELECT * FROM beans;").fetchall())

