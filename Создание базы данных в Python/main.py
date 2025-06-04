# 1. Импортировать DB-API 2.0 интерфейс (библиотеку sqlite3)
import sqlite3

conn = sqlite3.connect('MyDB.db') # Создать подключение к базе данных SQLite

cursor = conn.cursor() # Создать объект курсора

cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER
                )""") # Создать таблицу в базе данных:

conn.close() # Закрыть соединение с базой данных


def add_tables_on_db(x):
    conn = sqlite3.connect('MyDB.db')
    cursor = conn.cursor()

# Выполняем запрос на добавление новых столбцов в таблицу users
    cursor.execute(f"""ALTER TABLE users ADD COLUMN {x} TEXT""")
    print(f'add tables {x}')
# Сохраняем изменения и закрываем соединение с базой
    conn.commit()
    conn.close()


def show_tables_name():
# создаем соединение с нашей базой данных
    conn = sqlite3.connect('MyDB.db')
    cursor = conn.cursor()

# получаем метаданные для таблицы
#     cursor.execute("PRAGMA table_info(users)")
    cursor.execute("SELECT * FROM users")

# выводим названия полей таблицы
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    conn.close() # закрываем соединение с базой данных


def adding_records_to_the_database(name, age, surname, faculty, city):
    '''Добавление записей в БД'''
    conn = sqlite3.connect('MyDB.db')    # устанавливаем соединение с базой данных
    cursor = conn.cursor()               # создаем курсор для выполнения операций с базой данных

    cursor.execute(f'INSERT INTO users (name, age, surname, faculty, city) VALUES (?,?,?,?,?)', (name, age, surname, faculty, city))
    print('Success!')
    conn.commit()
    conn.close()


def main():
    print('Для просмотра таблиц 2\nДля записа БД 1')
    x = int(input('1-2: '))
    if x == 1:
        adding_records_to_the_database(name=input('Введите имя: '),
                                       age=int(input('Введите возраст: ')),
                                       surname=input('Введите фамилию: '),
                                       faculty=input('faculty: '),
                                       city=input('Введите свой город: '))
    elif x == 2:
        show_tables_name()


if __name__ == "__main__":
    main()


