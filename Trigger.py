import database

NEW_BEAN_TRIGGER = """
CREATE TRIGGER New Bean
AFTER INSERT ON reviews
BEGIN
INSERT INTO beans (name) VALUES (?);
END;"""


def new_bean_trigger(connection, name):
    with connection:
        connection.execute(NEW_BEAN_TRIGGER, (name,))
