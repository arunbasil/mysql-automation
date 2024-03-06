import random
import datetime
from db.connection import create_db_connection
from utilities.queries import insert_data


def generate_and_insert_dummy_data(connection, num_records):
    names = ["John Doe", "Jane Doe", "Alice Brown", "Bob Smith", "Charlie Davis"]
    for i in range(num_records):
        id = i
        current_datetime = datetime.datetime.now()  # Rename the variable here
        name = random.choice(names)
        insert_data(connection, id, current_datetime, name)  # Update the reference here



connection = create_db_connection()
generate_and_insert_dummy_data(connection, 10)

