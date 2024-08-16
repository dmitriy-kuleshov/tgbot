import psycopg2
from config import host, user, db_name, password

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )

        print(f"Server version: {cursor.fetchone()}")
except Exception as _ex:
    print("[INFO] Error with PostgreSQL(ZZZ)", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PG connection closed (ZZZ)")