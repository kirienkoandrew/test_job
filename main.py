print('''Вас приветствует программа определения координат.
Чтобы зайти в настройки нажмите 1
Чтобы определить координаты, введите адрес
''')

from dadata import Dadata

token = input('Введите token')
secret = input('Введите secret')
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
