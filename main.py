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
        cursor.execute(
            "SELECT version();"
        )
        print(f'Server vers: {cursor.fetchone()}')

    #create table
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE discount(
                discount_id PRIMARY KEY,
                 value numeric,
                 FOREIGN KEY (value) REFERENCES goods (size));"""
        )
        print("[INFO] Table created success")

    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO discount(value) VALUES (0.70),
                (0.50), (0.30);"""
        )
        print("[INFO] Data INSERT success")

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE goods(
                goods_id PRIMARY KEY,
                 name varchar(80),
                 size numeric,
                 description varchar(80),
                 calory numeric,
                 protein numeric
                 fat numeric,
                 weight numeric,
                 price numeric,
                 categorie_id int,
                 discount_id int,                
                 FOREIGN KEY (size) REFERENCES good_size (size_id),
                 FOREIGN KEY (discount_id) REFERENCES discount (value),
                 FOREIGN KEY (categorie_id) REFERENCES category (categorie_id));"""
        )
        print("[INFO] Data INSERT success")

    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO goods(name,size,description,calory,protein,fat,weight,price) 
            VALUES ('peperoni',30, 'spice', 500,10,5,700,17.50),
                ('studentskaya',35, 'not spice', 400,15,10,600,14.50), ('kaproch',25, 'not spice', 620,12,4,800,19.50);"""
        )
        print("[INFO] Data INSERT success")


except Exception as _ex:
    print('[INFO] Error while working with posgres', _ex)
finally:
    if connection:
        connection.close()
        print('[INFO] PostgreSQL connection close')