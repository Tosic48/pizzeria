import psycopg2

try:
    #connect to exist db
    connection = psycopg2.connect(
        host = '127.0.0.1',
        user = 'postgres',
        password = 'psql',
        database = 'pizza'
    )

    connection.autocommit = True

    #curs for perfoming
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f'Server vers: {cursor.fetchone()}')

    # create table size
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE size(
                size_id SERIAL PRIMARY KEY,
                 value numeric
                 /*FOREIGN KEY (value) REFERENCES goods (size)*/);"""
        )
        print("[INFO] Table size created success")

    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO size(value) VALUES (30),(40),(50);"""
        )
        print("[INFO] Data INSERT in size success")

    #create table goods
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE goods(
                goods_id SERIAL PRIMARY KEY,
                 name varchar(80),
                 size integer,
                 description varchar(80),
                 calory numeric,
                 protein numeric,
                 fat numeric,
                 weight numeric,
                 price numeric,
                 categorie_id INTEGER,
                 discount_id INTEGER                
                 /*FOREIGN KEY (size) REFERENCES good_size (size_id),
                 FOREIGN KEY (discount_id) REFERENCES discount (value),
                 FOREIGN KEY (categorie_id) REFERENCES category (categorie_id)*/);"""
        )
        print("[INFO] Created goods success")

    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO goods(name,size,description,calory,protein,fat,weight,price) 
            VALUES ('peperoni',30, 'spice', 500,10,5,700,17.50),
                ('studentskaya',35, 'not spice', 400,15,10,600,14.50), ('kaproch',25, 'not spice', 620,12,4,800,19.50);"""
        )
        print("[INFO] Data INSERT in goods success")

    #create table discount
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE discount(
                discount_id SERIAL PRIMARY KEY,
                 value numeric
                 /*FOREIGN KEY (value) REFERENCES goods (size)*/);"""
        )
        print("[INFO] Table discount created success")

    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO discount(value) VALUES (0.70),(0.50);"""
        )
        print("[INFO] Data INSERT in discount success")

    #create table good_size
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE good_size(
                good_size_id SERIAL PRIMARY KEY,
                 size_id integer,
                 good_id integer,
                 FOREIGN KEY (good_id) REFERENCES size (size_id)
                 /*FOREIGN KEY (size_id) REFERENCES goods (size)
                 FOREIGN KEY (value) REFERENCES goods (size)*/);"""
        )
        print("[INFO] Table good_size created success")

    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO good_size(size_id,good_id) VALUES (1,1),(2,2),(3,3);"""
        )
        print("[INFO] Data INSERT in good_size success")

    #create table category
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE category(
                category_id SERIAL PRIMARY KEY,
                 name varchar(80)
                 /*FOREIGN KEY (value) REFERENCES goods (size)*/);"""
        )
        print("[INFO] Table category created success")

    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO category(name) VALUES ('большая'),('маленькая'),('средняя');"""
        )
        print("[INFO] Data INSERT in category success")


except Exception as _ex:
    print('[INFO] Error while working with posgres', _ex)
finally:
    if connection:
        connection.close()
        print('[INFO] PostgreSQL connection close')