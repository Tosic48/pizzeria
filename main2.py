import psycopg2
from config import host, user, password, db_name

try:
    # подключение к существующей БД
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True
    # курсор для предоставления операций над БД
    # cursor = connection.cursor()

    # проверка версии БД
    with connection.cursor() as cursor:
        cursor.execute(
            'select version();'
        )
        print(f'Server version: {cursor.fetchone()}')

    # создание таблицы size
    with connection.cursor() as cursor:
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS size(
            id serial PRIMARY KEY,
            name varchar(50));
            '''
        )
        print(f'Таблица size успешно создана!')


    with connection.cursor() as cursor:
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS category(
            id serial PRIMARY KEY,
            name varchar(50));
            '''
        )
        print(f'Таблица category успешно создана!')

    with connection.cursor() as cursor:
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS category(
            id serial PRIMARY KEY,
            name varchar(50));
            '''
        )
        print(f'Таблица category успешно создана!')

    with connection.cursor() as cursor:
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS discount(
            id serial PRIMARY KEY,
            value integer);
            '''
        )
        print(f'Таблица discount успешно создана!')


    with connection.cursor() as cursor:
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS goods(
            id serial PRIMARY KEY,
            name varchar(50),
            description text,
            calory integer,
            protein integer ,
            fat integer, 
            weight integer ,
            price integer ,
            category_id integer references category(id),
            discount_id integer references discount(id));
            '''
        )
        print(f'Таблица goods успешно создана!')

    with connection.cursor() as cursor:
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS goods_size(
            id serial PRIMARY KEY,
            goods_id integer references goods(id),
            size_id integer references size(id));
            '''
        )
        print(f'Таблица discount успешно создана!')


    # # вставка данных в таблицу
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         '''INSERT INTO users(firs_name, nick_name)
    #         VALUES ('Igor', 'proger3000');
    #         '''
    #     )
    #     print(f'Данные успешно добавлены!')
    #
    # # выборка данных из таблицы
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         '''SELECT nick_name FROM users WHERE firs_name = 'Igor';
    #         '''
    #     )
    #     print(cursor.fetchone())
    #
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         '''DROP TABLE users;
    #         '''
    #     )
    #     print('Таблица удалена!')

except Exception as e:
    print('Ошибка в процессе выполнения PostgresQL', e)
finally:
    if connection:
        cursor.close()
        connection.close()
        print('[INFO] PostgreSQL соединение закрыто!')