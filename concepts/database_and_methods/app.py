# static methods, classmethods and instance methods
# pseudo-code
import psycopg2
import os
# functions (to connect to the database)
def get_connection():
    connection = psycopg2.connect("dbname=november user=postgres")
    cur = connection.cursor()
    return connection, cur

def write_to_db(connection):
    connection.commit()


def connect_db():
    uri = os.environ.get(
        "DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/tdd_test"
    )
    connection = psycopg2.connect(uri)
    cur = connection.cursor()
    return connection, cur


class Human:
    # first name, last name
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name

    # walking(), eating(), greeting(), save()

    """
    fausto = Human('fausto', 'doe')
    fausto.save()
    """    
    def save(self):
        connection, cur = get_connection()
        # name -> first name and last name
        name = f"{self.first_name} {self.last_name}"
        cur.execute(f"INSERT INTO users(name) VALUES('{name}')")
        write_to_db(connection)

if __name__ == '__main__':
    test = connect_db()
    ##print(test)
    
    #h = Human('X', 'Y')
    
    #h.save()