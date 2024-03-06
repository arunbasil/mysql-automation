import pytest
from db.connection import create_connection

@pytest.fixture(scope="session")
def db_connection():
    connection = create_connection()
    yield connection
    connection.close()
