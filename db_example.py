import psycopg2
from handlers.config import host, user, db_name, password

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    # для создания таблицы в БД нужен коммит
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
# создание таблицы в БД
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE botskiy(
    #         id serial PRIMARY KEY,
    #         name varchar(50) NOT NULL)"""
    #     )
    #     print("[INFO] Table created successfully (ZZZ)")
# вставка данных в БД
#     with connection.cursor() as cursor:
#         cursor.execute(
#             """INSERT INTO botskiy (name) VALUES
#             ('zorobotskiy');"""
#         )
#
#         print("[INFO] Data was inserted successfully (ZZZ)")
# извлечение данных из БД
#     with connection.cursor() as cursor:
#         cursor.execute(
#             """SELECT name FROM botskiy WHERE id = 1;"""
#         )
#
#         print(cursor.fetchone())
#         print("[INFO] Data was inserted successfully (ZZZ)")


except Exception as _ex:
    print("[INFO] Error with PostgreSQL(ZZZ)", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PG connection closed (ZZZ)")
