
CREATE_BEAN_TABLE = """
CREATE TABLE IF NOT EXISTS beans (id INTEGER PRIMARY KEY, 
name TEXT);"""

NEW_BEAN_TRIGGER = """
CREATE TRIGGER NewBean
AFTER INSERT ON reviews
BEGIN
INSERT INTO beans (name) VALUES ();
END;"""


def new_bean_trigger(connection, name):
    with connection:
        connection.execute(NEW_BEAN_TRIGGER, (name,))
