import psycopg2


def define_postgres_connection(host: str, database: str, user: str, passwd: str):
    try:
        print("Connecting to RDS postgres")
        return psycopg2.connect(host=host, database=database, user=user, password=passwd)
    except psycopg2.DatabaseError as e:
        print("Unable to connect to postgres: " + str(e))
        raise


def process_query(connection, query_definition: str):
    print('Processing query')
    cursor = None

    try:
        print('Defining cursor')
        cursor = connection.cursor()

        print('Executing query')
        cursor.execute(query_definition)
        connection.commit()
    except Exception as e:
        print("Unable to process query: " + str(e))
        raise
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
