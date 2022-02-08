print('''Вас приветствует программа определения точных координат введенного адреса.
''')

from dadata import Dadata

import sqlite3

# создание таблицы
try:
    sqlite_connection = sqlite3.connect('settings.db')
    sqlite_create_table_query = '''CREATE TABLE settings (token TEXT, secret TEXT, lang TEXT DEFAULT ru, base_url TEXT DEFAULT https://dadata.ru/);'''

    cursor = sqlite_connection.cursor()
    # print("База данных подключена к SQLite")
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    # print("Таблица SQLite создана")

    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        # print("Соединение с SQLite закрыто")

# добавление данных в таблицу
try:
    sqlite_connection = sqlite3.connect('settings.db')
    cursor = sqlite_connection.cursor()
    # print("Подключен к SQLite")
    token = input('Введите API-ключ: ')
    secret = input('Введите секретный ключ: ')
    lang = 'ru'
    sqlite_insert_query = f"INSERT INTO 'settings' (token, secret, lang) VALUES ('{token}', '{secret}', '{lang}');"
    count = cursor.execute(sqlite_insert_query)
    sqlite_connection.commit()
    # print("Запись успешно вставлена в таблицу settings ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)
finally:
    if sqlite_connection:
        sqlite_connection.close()
        # print("Соединение с SQLite закрыто")


def read_sqlite_table():  # чтение строки из БД
    try:
        sqlite_connection = sqlite3.connect('settings.db')
        cursor = sqlite_connection.cursor()
        # print("Подключен к SQLite")

        sqlite_select_query = """SELECT * from settings"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        token, secret, lang = records[0][0], records[0][1], records[0][2]
        cursor.close()
        return token, secret, lang

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            # print("Соединение с SQLite закрыто")


def delete_sqlite_record():  # очищаем БД
    try:
        sqlite_connection = sqlite3.connect('settings.db')
        cursor = sqlite_connection.cursor()
        # print("Подключен к SQLite")
        cursor.execute('DELETE from settings;', )
        sqlite_connection.commit()
        # print("Запись успешно удалена")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            # print("Соединение с SQLite закрыто")


def update_sqlite_table(new_lang):  # изменение языка в таблице
    try:
        sqlite_connection = sqlite3.connect('settings.db')
        cursor = sqlite_connection.cursor()
        #print("Подключен к SQLite")

        sql_update_query = f"Update settings set lang = '{new_lang}'"

        cursor.execute(sql_update_query)
        sqlite_connection.commit()
        print("Запись успешно обновлена")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def update_sqlite_table_api(new_token, new_secret):  # изменения secret и token
    try:
        sqlite_connection = sqlite3.connect('settings.db')
        cursor = sqlite_connection.cursor()
        #print("Подключен к SQLite")
        sql_update_query = f"Update settings set token = '{new_token}', secret = '{new_secret}'"
        cursor.execute(sql_update_query)
        sqlite_connection.commit()
        print("Запись успешно обновлена")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def update_sqlite_table_url(new_url):  # изменения URL
    try:
        sqlite_connection = sqlite3.connect('settings.db')
        cursor = sqlite_connection.cursor()
        #print("Подключен к SQLite")
        sql_update_query = f"Update settings set base_url = '{new_url}'"
        cursor.execute(sql_update_query)
        sqlite_connection.commit()
        print("Запись успешно обновлена")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


token, secret, lang = read_sqlite_table()
dadata = Dadata(token, secret)


def result():
    token, secret, lang = read_sqlite_table()
    print('Введите адрес: ')
    results = dadata.suggest(name='address', query=input(), language=lang, count=20)

    if len(results) > 1:
        print('Список адресов по Вашему запросу:')
        for i, result in enumerate(results):
            print(f"{i + 1}. {result['value']}")
        print('Выберите нужный адрес: ')
        item = checker(results)
        while 1 > item or item > len(results):
            print('Введите число от 1 до ', len(results))
            item = checker(results)
        else:
            print(f"Координаты по адресу {results[item - 1]['value']}: ")
            print(f"широта: {results[item - 1]['data']['geo_lat']}, долгота: {results[item - 1]['data']['geo_lon']}")

            one_more_time()

    elif len(results) == 0:
        print('Ничего не найдено')
        one_more_time()
    elif len(results) == 1:
        print(f"Найден адрес {results[0]['value']}. Это то, что Вы искали?")
        if input('да/нет ').lower() == 'да':
            print(f"Координаты по адресу {results[0]['value']}: ")
            print(f"широта: {results[0]['data']['geo_lat']}, долгота: {results[0]['data']['geo_lon']}")
        else:
            one_more_time()

        one_more_time()


def one_more_time():
    res = input('Проверить другой адрес? да/нет. Для изменения настроек введите settings ')
    if res.lower() == 'да':
        result()
    elif res == 'settings':
        print('''Что хотите изменить?
1. Базовый URL к сервису dadata
2. API ключ для сервиса dadata
3. Язык, на котором должен возвращаться ответ от dadata
Если передумали менять, введите 0
''')
        settings_input = int(input())
        if settings_input == 1:
            input_new_url = input('Введите новый URL: ')
            update_sqlite_table_url(input_new_url)
            one_more_time()
        elif settings_input == 2:
            input_token = input('Введите новый API-ключ: ')
            input_secret = input('Введите новый секретный ключ: ')
            update_sqlite_table_api(input_token, input_secret)
            one_more_time()
        elif settings_input == 3:
            while True:
                print('Введите ru или en')
                item = input()
                if item in ['ru', 'en']:
                    update_sqlite_table(item)
                    one_more_time()
                else:
                    print('Неверный ввод.')
        else:
            one_more_time()
    else:
        delete_sqlite_record()
        exit()


def checker(results_list):
    while True:
        try:
            item = int(input())
        except:
            print('Введите число от 1 до ', len(results_list))
        else:
            return item


result()
