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

CREATE - Создание
ALTER - обновление
DROP - удалять

