from postgres_client import process_query, define_postgres_connection
from sql_definition import define_query


def lambda_handler(event, context):
    message = ""

    rds_host = "rds-postgres-host.66cezfdpmr.eu-west-1.rds.amazonaws.com"
    rds_db_name = "rds-postgres-db"
    master_user = "master"
    master_pwd = "master-pass"

    try:
        process_query(
            define_postgres_connection(rds_host, rds_db_name, master_user, master_pwd),
            define_query(rds_db_name)
        )

        message += "Success"

    except Exception as e:
        message += "Error during an operation: " + str(e)

    return {'message': message}
