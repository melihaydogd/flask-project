import psycopg2

dbname = "postgres"
user = "user"
password = "password"
host = "localhost"
port = "5432"

def get_connection():
    try:
        connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        return connection
    except psycopg2.OperationalError as e:
        print(f"Error: {e}")
        exit(1)

def execute_query(connection, query, parameters):
    cursor = connection.cursor()
    cursor.execute(query, parameters)
    result = cursor.fetchall()
    cursor.close()
    return result

def close_connection(connection):
    connection.close()