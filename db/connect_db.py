import psycopg2

# Connection details
host = "localhost"
port = "5001"
database = "PythonDB"
user = "postgres"
password = "byronodmon"

def connect():
    return psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )