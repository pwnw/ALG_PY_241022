"""
Задание 1.
Реализуйте функции:
a) заполнение списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   заполнение словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
b) получение элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   получение элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
с) удаление элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   удаление элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""

from time import time

n = 10 ** 5

# Пункт А
def time_decorator(func):
    def timer(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'Время выполенения функции {func.__name__} '
              f'составило {end - start}')
        return result

    return timer


@time_decorator
# Сложность O(n)
def fill_list(lst, num):
    for i in range(num):
        lst.append(i)


some_list = []
fill_list(some_list, n)
print('_' * 100)


@time_decorator
# Сложность O(n)
def fill_dict(dct, num):
    for i in range(num):
        dct[i] = i


some_dict = {}
fill_dict(some_dict, n)
print('_' * 100)


"""
Время выполенения функции fill_list составило 0.012964725494384766
_______________________________________________________________________________
Время выполенения функции fill_dict составило 0.007947921752929688
_______________________________________________________________________________
Вывод: список заполняется быстрее, поскольку словарь требует вычисление хешей
"""

# Пункт Б
@time_decorator
# Сложность O(1)
def get_el_list(lst):
    for j in range(20000):
        lst[j] = lst[j + 1]


get_el_list(some_list)
print('_' * 100)


@time_decorator
# Сложность O(1)
def get_el_dict(dct):
    for j in range(1, 20001):
        dct[j] = 'a'


get_el_dict(some_dict)
print('_' * 100)


"""
Время выполенения функции get_el_list составило 0.0020265579223632812
____________________________________________________________________________________________________
Время выполенения функции get_el_dict составило 0.0009918212890625
____________________________________________________________________________________________________
Вывод: Получение и изменение элемента у словаря происходи быстрее, чем у списка
"""

# Пункт C
@time_decorator
# Сложность O(n)
def del_el_list(lst):
    for i in range(10000):
        lst.pop(i)


del_el_list(some_list)
print('_' * 100)


@time_decorator
# Сложность O(1)
def del_el_dict(dct):
    for i in range(10000):
        dct.pop(i)


del_el_dict(some_dict)
print('_' * 100)


"""
Время выполенения функции del_el_list составило 0.24933385848999023
____________________________________________________________________________________________________
Время выполенения функции del_el_dict составило 0.0009968280792236328
____________________________________________________________________________________________________
Вывод: Удаление элемента у словаря происходи быстрее, чем у списка так как в списке все элементы после удаления
сдвигаются
"""




"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш
Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей
ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""

import csv
import os.path
from binascii import hexlify
from hashlib import pbkdf2_hmac

CSV = 'password_hash.csv'  # файл в котором находятся данные


def hash_function(login_def, password_def):
    password_hash = hexlify(
        pbkdf2_hmac(hash_name='sha256', salt=login_def.encode('utf-8'), password=password_def.encode('utf-8'),
                    iterations=100000))
    return password_hash


# Проверка пароля
def password_verification(login_def, password_input):
    password_input = str(hash_function(login_def, password_input))
    print(f'Хеш введенного только что пароля: {password_input}')
    with open(CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            password_in_csv = row.get(login_def)
            break
    if password_in_csv == password_input:
        return f'Добро пожаловать, {login_def}'
    else:
        return exit('Неверный пароль!')


# Если файл отсутствует в системе, то создаем его и заполняем шаблонными данными.
def added_password_hash_file():
    users = ['Aleksey', 'Oleg', 'Ivan']
    passwords = ['11111', '22222', '33333']
    for i in range(len(passwords)):
        passwords[i] = hash_function(users[i], passwords[i])
    users_and_password = dict(zip(users, passwords))
    with open(CSV, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=users)
        writer.writeheader()
        writer.writerow(users_and_password)


if not os.path.exists(CSV):
    added_password_hash_file()

login = 'Aleksey'
print(f'Здравствуйте, {login}!')
password = input('Введите пароль: ')
print(password_verification(login, password))


"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции
Дана строка S длиной N, состоящая только из строчных латинских букв
Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.
Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.
Пример:
рара - 6 уникальных подстрок
рар
ра
ар
ара
р
а
"""


import hashlib


def number_of_unique(row_def):
    unique_substrings = set()
    for i in range(1, len(row_def)):
        for j in range(len(row_def) - i + 1):
            res = hashlib.sha256(row_def[j:j + i].encode('utf-8')).hexdigest()
            unique_substrings.add(res)
            print(row_def[j:j + i], end=' ')
    return len(unique_substrings)


row = input('Введите строку: ')
print(f'\nВ строке {row} {number_of_unique(row)} уникальных подстрок')


"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
есть ли в кэше соответствующая страница или нет
Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}
Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""


from uuid import uuid4
import hashlib

salt = uuid4().hex
cache_obj = {}


def get_page(url):
    if cache_obj.get(url):
        print(f'Данный адрес: {url} присутствует в кэше')
    else:
        res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cache_obj[url] = res
        print(cache_obj)


get_page('https://geekbrains.ru/')
get_page('https://geekbrains.ru/')