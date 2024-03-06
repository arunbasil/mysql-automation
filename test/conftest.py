import pytest
from db.connection import create_db_connection

@pytest.fixture(scope="module")
# The db_connection fixture is scoped to the module, meaning it will be created once per test module and shared across tests in that module. 
def db_connection():
    # Setup: create the database connection
    connection = create_db_connection()
    yield connection
    # Teardown: close the database connection
    if connection:
        connection.close()

@pytest.fixture(scope="function")
# The db_cursor fixture is function-scoped (the default scope), meaning it will be created and destroyed for each test function.
def db_cursor(db_connection):
    # Setup: create a cursor from the database connection
    cursor = db_connection.cursor()
    yield cursor
    # Teardown: close the cursor
    cursor.close()

