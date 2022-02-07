print('''Вас приветствует программа определения координат.
Чтобы зайти в настройки нажмите 1
Чтобы определить координаты, введите адрес
Чтобы выйти наберите 'выход'
''')

from dadata import Dadata
token = "960470cc092b3e78097ec9065f65fd730d25c7e4"
secret = "14f9058d46c8a1232ccc2b7d8e31433daa19447a"
dadata = Dadata(token, secret)

print('Введите адрес: ')

results = dadata.suggest(name="address", query='Ленина 8')

print()

if len(results) > 1:
    for i, result in enumerate(results):
        print(i + 1, result)
    print('Выберите верный адрес: ')
    item = int(input())
    print(results[item - 1])
    print(results[item - 1]['data']['geo_lat'], results[item - 1]['data']['geo_lon'])
elif len(results) == 0:
    print('Ничего не найдено')
elif len(results) == 1:
    print(results)
    print(results[0]['data']['geo_lat'], results[0]['data']['geo_lon'])
    #print(result['value'])
#print(result['geo_lat'], result['geo_lon'])
