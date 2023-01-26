import psycopg2
from config import host, user, password, db_name


try:
    #connect to exist db
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
    )

    #curs for perfoming
    with connection.cursor() as cursor:
        pass

except Exception as _ex:
    print('[INFO] Error while working with posgres', _ex)
finally:
    if connection:
        connection.close()
        print('[INFO] PostgreSQL connectio