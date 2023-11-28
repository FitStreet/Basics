\с - подключение к бд
\du - показывает всех пользователей
\dt - показывает все таблицы внутри БД
\d <название таблтицы> - подробная информация о таблице
\l - показывает весь список баз данных
\q - выход из СУБД

sudo -u postgres psql - команда для входа через юзера postgres
CREATE USER <username> WITH PASSWORD "password";

CREATE USER 
<username> 
WITH PASSWORD 
"password";

ALTER ROLE <username> <привилегии>;
CREATE DATABASE <username> WHITH OWNER <username>;

int:
    bigint - 8ми байтные числа
    integer - 4х байтовое число
    smallint - 2х байтовое число 
    serial - автоинкрементация
str:    
    char(10) - фикс длина строки
    varchar(10) - фикс длина строки 
    text - без ограничений по кол-ву символов
<!-- char | varchar -->

date:
    timestamp - дата и время
    time - время
    date - дата

boolean - true|false

CREATE DATABASE <название БД>
CREATE TABLE <название таблицы>(
    column1 varchar NOT NULL
)

create table product (
id serial primary key,
name varchar(40) not null,
price int check (price > 0));

CREATE - Создание
ALTER - обновление
DROP - удалять

primary key
foreing key
unique
null
not null
check() - для проверки данных

"""Заполнение таблицы"""
insert into <название таблицы> (<столбец 1><столбец 2>) values ('значение 1' 'значение 2')
insert into product (name,price) values ('Iphone 14', 24000);
insert into product (price, name) values (16000,'Iphone 17');
insert into product (name,price) values ('Iphone 13', 24000),
shop_db-# ('Iphone 5', 5000), ('MacBookAir', 74000);
insert into product (name) values ('oooo');

### Вывод данных из таблицы
select * from <название таблицы> - выводит все содержимое таблицы

### Условия
ORDER BY - сортирует данные по убыванию или возрвстанию
ASC(по возрастанию)
DESC(по убыванию)

select * from product ORDER BY id;
select * from product ORDER BY id desc;

LIMIT - возвращает ограниченное количество данных
select * from product limit 5;

OFFSET - пропускает несколько записей
select * from product order by price offset 2;(пропустит 2 записи вначале)

DISTINCT - убирает дубликаты и возвращает только уникальные значения
select distinct price from product;

WHERE - фильтрацияпо каким-то критериям
<!-- >, <, >=, <=, =, != -->
or - 
and - 
not - 
in - 
BETWEEN - диапозон

LIKE - выводит результат, который подходит введенному шаблону(чувствителен к регистру)
ILIKE - выводит результат, который подходит введенному шаблону(не чувствителен к регистру)

where name like 'A%' - выведет все имена нач на A
where name like '@gmail.com' - найдет все что заканчивается на @gmail.com
where name like '%A%' - найдет все где в середине есть A

select name from product where name ilike '%iphone%';

### Удаление данных из таблицы
delete * from product; удалится все

<!-- сделать update -->





