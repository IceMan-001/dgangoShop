from django.test import TestCase
from django.core.paginator import Paginator
# Create your tests here.
women = ['Анджелина Джоли', 'Дженнифер Лоуренс', 'Джулия Робертс', 'Марго Робби', 'Ума Турман', 'Ариана Гранде', 'Бейонсе', 'Кэтти Перри', 'Рианна', 'Шакира']

p = Paginator(women, 3)

print(p)