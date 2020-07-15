# ARGUMENTS:
# rds_db_name: {0}

SQL = """
DO
$do$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_database WHERE datname = '{0}') THEN
      CREATE DATABASE {0} LC_COLLATE 'C' TEMPLATE template0 ENCODING 'UTF8';
   END IF;
END
$do$;
"""


def define_query(rds_db_name: str) -> str:
    print('Defining SQL query')
    try:
        return SQL.format(rds_db_name)
    except Exception:
        print('Error during SQL query definition')
        raise
