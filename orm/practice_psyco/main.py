#ORM технология позволяющая автоматически связать бд с кодом
# psycopg2 - библиотека которая предоставляет итерфейс Python для взаимодействия с PostgreSQL

import psycopg2

db_params = {
    'host':'localhost',
    'database':'practice_psyco',
    'user':'fitstreet',
    'password':'Stdvan1x'
}

connection = psycopg2.connect(**db_params)

create_table = """
CREATE TABLE test(
id serial primary key,
name varchar(30),
age int
)
"""

data = ('Nikita', 20)
data2 = ('Ivan', 32)

data = [('Nikita', 20), ('Nikita', 20), ('Nikita', 20), ('Nikita', 20)]
insert_query = f"""
insert into test(name, age) values {data};
"""
insert_query = """
insert into test(name, age) values (%s, %s);
"""
select_query = """
select * from test;
"""
data = ('sherlok', 20)
update_query = """
update test set name = %s where id = %s;
"""
del_id = 1

delete_query = f"""
delete from test where id = {del_id};
"""

try:
    cursor = connection.cursor()
    # cursor.execute()
    cursor.execute(select_query) # выполнение sql запроса
    connection.commit()
    results = cursor.fetchall()
    print(results)
finally:
    cursor.close()
    connection.close()

# peewee
# sqlalchemy
