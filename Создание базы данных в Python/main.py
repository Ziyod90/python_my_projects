# 1. Импортировать DB-API 2.0 интерфейс (библиотеку sqlite3)
import sqlite3

conn = sqlite3.connect('MyDB.db') # Создать подключение к базе данных SQLite

cursor = conn.cursor() # Создать объект курсора

cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                surname TEXT,
                faculty TEXT,
                city TEXT
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


def update_user_interactive():
    conn = sqlite3.connect('MyDB.db')
    cursor = conn.cursor()

    user_id = input("Введите ID пользователя, которого хотите обновить: ")

    # Получим текущие данные пользователя (для проверки)
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()

    if not user:
        print("❌ Пользователь с таким ID не найден.")
        conn.close()
        return

    print(f"\n🔍 Текущие данные пользователя: {user}\n")

    # Предложим выбор поля для обновления
    fields = ["name", "age", "surname", "faculty", "city"]
    print("Выберите поле для обновления:")
    for i, field in enumerate(fields, start=1):
        print(f"{i}. {field}")

    choice = int(input("Введите номер поля (1-5): "))
    if choice < 1 or choice > len(fields):
        print("❌ Неверный выбор.")
        conn.close()
        return

    field_to_update = fields[choice - 1]
    new_value = input(f"Введите новое значение для поля '{field_to_update}': ")

    # Приведение типа, если это возраст
    if field_to_update == "age":
        try:
            new_value = int(new_value)
        except ValueError:
            print("❌ Возраст должен быть числом.")
            conn.close()
            return

    # Обновляем поле
    cursor.execute(f"UPDATE users SET {field_to_update} = ? WHERE id = ?", (new_value, user_id))
    conn.commit()
    conn.close()

    print(f"✅ Поле '{field_to_update}' успешно обновлено для пользователя с ID = {user_id}.")


def main():
    print('для отображения всех записей из базы данных нажмите 1\nДля записа в БД нажмите 2\nДля обновление данных в БД нажмите 3')
    x = int(input('1-2: '))
    if x == 2:
        adding_records_to_the_database(name=input('Введите имя: '),
                                       age=int(input('Введите возраст: ')),
                                       surname=input('Введите фамилию: '),
                                       faculty=input('faculty: '),
                                       city=input('Введите свой город: '))
    elif x == 1:
        show_tables_name()
    elif x == 3:
        update_user_interactive()


if __name__ == "__main__":
    main()


