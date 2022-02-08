# test_job
Программа определения точных координат введенного адреса
Пользователь вводит API-ключ и секретный ключ который он получил при регистрации на сервисе https://dadata.ru/profile/#info

Далее пользователю предоставляется поле ввода адреса
После ввода адреса, если результаты не найдены, получаем сообщение «Ничего не найдено»
Если найден только один адрес, пользователю задается вопрос «Это то, что Вы искали?». Если ответ да, то отображаются координаты заданного адреса, если нет, то предлагается ввести другой адрес.
Если адресов найдено несколько, то пользователю предоставляется нумерованный список адресов (максимум 20) из которого он может выбрать только один, указав в поле ввода его порядковый номер. Далее, отображаются координаты этого адреса.

Также, после вывода координат, пользователь может зайти в настройки, после отображения сообщения «Проверить другой адрес? да/нет. Для изменения настроек введите settings» введя settings, дальше отображается список настроек, которые можно изменить:
	1. Базовый URL к сервису dadata
	2. API ключ для сервиса dadata
	3. Язык, на котором должен возвращаться ответ от dadata
После ввода соответствующей цифры, предоставляется возможность ввода новых данных. В случае успешного изменения, отображается сообщение об успехе.
