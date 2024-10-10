"""Datetime включает в себя разные классы, позволяющие получать нужные временные данные:

datetime.date: день, месяц и год;
datetime.time: время в часах, минутах, секундах, а также микросекундах. Тут дата значения не имеет;
datetime.datetime: здесь хранятся атрибуты date и time."""
# https://otus.ru/journal/tekushhaya-data-i-vremya-v-python/

from datetime import datetime, date

# функция now() — она позволит получить объект с текущим временем и датой.
current_datetime = datetime.now()

print(current_datetime)  # 2024-07-17 13:51:27.820816
print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)

current_date = datetime.now().date()
print(current_date)  # 2024-07-17

current_date = date.today()
print(current_date)  # 2024-07-17

current_date = current_date.weekday()+1
print(current_date)  # 3 (среда)
