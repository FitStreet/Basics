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

UPDATE <имя_таблицы>
SET столбец1 = новое_значение1, столбец2 = новое_значение2, ...
WHERE условие;

UPDATE product set name = 'iphone 18' where id = 3;

AS

select name, price / 89 as dollars from product ;

GROUP BY - ключевое слово которое позволяет выводить значения из колонок объединенные в группы 

select name, sum(price) from product group by name;

HAVING - точно так же как WHERE но всегда используется с GROUP BY, выводит результат условия для групп
WHERE - выводит результат условия для строк
select name, sum(price) from product
where price < 24000 
group by name 
having name = 'Iphone 5';

### Связи

One to One - один к одному(User - User_id, один человек - один мозг, однастрана - один флаг)

One to Many - один ко многим(одна книга - много страниц, один куратор - много студентов, один автор - много книг)

Many to many - многие ко многим (много аккайнтов - много репозиториевб многопредметов - много учеников, много запчастей - много машин)

PRIMARY KEY - внешний ключ, с помощью него создаются связи

FOREING KEY - первичный ключ, ссылается на PRIMARY KEY

one to one - к id другой таблицы даем уникальность
one to many - создаем id другой таблицы
many to many - создаем третью таблицу в которой ссылаемся на две связвнные таблицы

select * from book where title = 'test'; не оптимизировано

### Индексы
Индексы - это спец объекты, предназначенные в основном для ускорения доступа к данным 

btree

        31 - корень(узел)
    12      31 - потомки узла(ветки)
6     18  26    43 - (листья)

Типы индексов в postgre
1. b-дерево Balanced tree
2. хеш
3. gist
4. spgist
5. gin
6. brin

 create index book_title on book (title);
 drop index

SELECT character.charname, speechcount,work.title FROM character LEFT JOIN character_work ON character.charid = character_work.charid LEFT JOIN work ON character_work.workid = work.workid;

### JOIN

join - инструкция, которая позволяет в запросах select брать данные из нескольких таблиц

INNER JOIN (JOIN) - достает только те записи у которых есть связь
select cat.name, shelter.title from cat join shelter on cat.id = shelter.cat_id;
  name  |  title
--------+----------
 barsik | shelter1
 noname | shelter2

LEFT JOIN - достает все записи с левой таблицы и соединяет с правой таблицейвозвращает все строки из левой таблицы и только совпадающие строки из правой таблицы

select cat.name, shelter.title from cat left join shelter on cat.id = shelter.cat_id;

  name   |  title
---------+----------
 barsik  | shelter1
 noname  | shelter2
 kiska   |
 lucifer |

RIGHT JOIN -  возвращает все строки из правой таблицы и только совпадающие строки из левой таблицы

select cat.name, shelter.title from cat right join shelter on cat.id = shelter.cat_id;

  name  |  title
--------+----------
 barsik | shelter1
 noname | shelter2
        | shelter3
        | shelter4

<!-- левая таблица до JOIN а правая после -->
FULL JOIN - достает все записи с обеих таблиц

select cat.name, shelter.title from cat full join shelter on cat.id = shel
ter.cat_id;

  name   |  title
---------+----------
 barsik  | shelter1
 noname  | shelter2
         | shelter3
         | shelter4
 kiska   |
 lucifer |

SELF JOIN

#Элиас - select c.name , s.title from cat as c join shelter as s on c.id = s.cat_id; можно забать свои названия через AS

### import/export database

psql -U <username> -d <название бд> -f <название файла>
<название бд> должно существовать в бд

создание файла.
pg_dump <название бд которую хотим перенести в файл> > <путь к файлу и/или название файла>
pg_dump -U <юзернэйм> <название бд которую хотим перенести в файл> > <путь к файлу и/или название файла>

### агрегатные функции

SUM - функция считающая сумму всех записей.

select c.name, sum(p.price) as total_price from customer as c join orders as o on c.id = o.customer_id join products as p on p.id = o.products_id group by c.name
 order by total_price;

MIN/MAX - находит минимальное и максимальное значение среди записей в сгруппированном поле 

COUNT - считает количество записей в сгруппированном поле

