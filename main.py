print('''Вас приветствует программа определения координат.
Чтобы зайти в настройки нажмите 1
Чтобы определить координаты, введите адрес
''')

from dadata import Dadata

# import sqlite3
#
# connection = sqlite3.connect('settings.db')
# cursor = connection.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS Settings
#               (token TEXT, secret TEXT, lang TEXT)''')
#
# cursor.execute(
#     "INSERT INTO Settings VALUES ('Stranger Things', 'Shawn Levy', 2016)")
# cursor.execute("SELECT * FROM Shows")
#
# print(cursor.fetchone())
#
# connection.commit()
# connection.close()

#создание таблицы
import sqlite3

try:
    sqlite_connection = sqlite3.connect('settings.db')
    sqlite_create_table_query = '''CREATE TABLE settings (token TEXT, secret TEXT, lang TEXT);'''

    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    print("Таблица SQLite создана")

    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")

#добавление данных в таблицу
try:
    sqlite_connection = sqlite3.connect('settings.db')
    cursor = sqlite_connection.cursor()
    print("Подключен к SQLite")
    token = input('Введите token')
    secret = input('Введите secret')
    lang = input('Введите lang')
    sqlite_insert_query = f"INSERT INTO 'settings' (token, secret, lang) VALUES ('{token}', '{secret}', '{lang}');"
    count = cursor.execute(sqlite_insert_query)
    sqlite_connection.commit()
    print("Запись успешно вставлена в таблицу settings ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")

def read_sqlite_table(): # чтение строки из БД
    try:
        sqlite_connection = sqlite3.connect('settings.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_select_query = """SELECT * from settings"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Всего строк:  ", len(records))
        print(records)
        # for row in records:
        #     print("Token:", row[0])
        #     print("Secret:", row[1])
        #     print("Lang:", row[2], end="\n\n")
        token, secret, lang = records[0][0], records[0][1], records[0][2]
        cursor.close()
        return token, secret, lang

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def delete_sqlite_record(): # очищаем БД
    try:
        sqlite_connection = sqlite3.connect('settings.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        #sql_update_query = """DELETE from settings where id = ?"""
        cursor.execute('DELETE from settings;',)
        sqlite_connection.commit()
        print("Запись успешно удалена")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")



# token = input('Введите token')
# secret = input('Введите secret')
token, secret, lang = read_sqlite_table()
dadata = Dadata(token, secret)

print('Введите адрес: ')

results = dadata.suggest(name="address", query='Ленина 8')

print()


def result():
    if len(results) > 1:
        for i, result in enumerate(results):
            print(i + 1, result)
        print('Выберите нужный адрес: ')
        item = checker(results)
        while 1 > item or item > len(results):
            print('Введите число от 1 до ', len(results))
            item = checker(results)
        else:
            print(results[item - 1])
            print(results[item - 1]['data']['geo_lat'], results[item - 1]['data']['geo_lon'])
            one_more_time()

    elif len(results) == 0:
        print('Ничего не найдено')
        one_more_time()
    elif len(results) == 1:
        print(results)
        print(results[0]['data']['geo_lat'], results[0]['data']['geo_lon'])
        one_more_time()


def one_more_time():
    if input('Еще раз? да/нет  ').lower() == 'да':
        result()
    else:
        delete_sqlite_record()
        exit()


def checker(results):
    while True:
        try:
            item = int(input())
        except:
            print('Введите число от 1 до ', len(results))
        else:
            return item


result()
