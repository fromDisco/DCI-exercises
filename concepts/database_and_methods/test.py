def connect_db():
    uri = os.environ.get(
        "DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/tdd_test"
    )
    connection = psycopg2.connect(uri)
    cur = connection.cursor()
    return connection, cur