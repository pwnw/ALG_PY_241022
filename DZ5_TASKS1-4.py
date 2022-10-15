"""
Задание 1.
Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего
Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections
Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235
Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34
Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""

from collections import Counter


companies_profits = Counter()
number_of_companies = int(input("Введите количество предприятий для расчета прибыли: "))
summ_profit = 0
for i in range(number_of_companies):
    company_name = input("Введите название предприятия: ")
    profits = input("Через пробел введите прибыль данного предприятия\nза каждый "
                    "квартал (всего 4 квартала), и нажмите Enter: ").split(' ')
    if len(profits) != 4:
        print('Не верный ввод')
    for profit in profits:
        profit = float(profit)
        companies_profits[company_name] += profit
        summ_profit += profit

average_profit = summ_profit / (number_of_companies)


print("Средняя годовая прибыль всех предприятий: {}".format(average_profit))
print("Предприятия, с прибылью выше среднего значения: {}".format(" ".join(
    filter(lambda x: companies_profits[x] > average_profit, companies_profits.keys())
    )))
print("Предприятия, с прибылью ниже среднего значения: {}".format(" ".join(
    filter(lambda x: companies_profits[x] < average_profit, companies_profits.keys())
    )))


    """
Задание 2.
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections
defaultdict(list)
int(, 16)
reduce
2) через ООП
вспомните про перегрузку методов
__mul__
__add__
"""

'''
pass
Допишу позже
'''

"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list
Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее
2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее
3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее
Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""

from timeit import timeit
from collections import deque

my_lst = [i for i in range(1001)]
my_deq = deque(my_lst)


# 1)
# append
def lst_append():
    for i in range(1001):
        my_lst.append(i)
    return my_lst

def deq_append():
    for i in range(1001):
        my_deq.append(i)
    return my_deq


# pop
def lst_pop():
    for i in range(1001):
        my_lst.pop()
    return my_lst

def deq_pop():
    for i in range(1001):
        my_deq.pop()
    return my_deq


# extend
def lst_extend():
    for i in range(1001):
        my_lst.extend([1, 2, 3])
    return my_lst

def deq_extend():
    for i in range(1001):
        my_deq.extend([1, 2, 3])
    return my_deq


print('-append-')
print('lst', timeit('lst_append()', globals=globals(), number=1000))
print('deq', timeit('deq_append()', globals=globals(), number=1000), '\n')
print('-pop-')
print('lst', timeit('lst_pop()', globals=globals(), number=1000))
print('deq', timeit('deq_pop()', globals=globals(), number=1000), '\n')
print('-extend-')
print('lst', timeit('lst_extend()', globals=globals(), number=1000))
print('deq', timeit('deq_extend()', globals=globals(), number=1000), '\n')

'''
Резльтат замеров следущий: время выполнения операций практически совпадает, очередь незначительно быстрее.
'''


# 2)
# appendleft
def lst_appendleft():
    for i in range(101):
        my_lst.insert(0, i)
    return my_lst

def deq_appendleft():
    for i in range(101):
        my_deq.appendleft(i)
    return my_deq


# popleft
def lst_popleft():
    for i in range(1):
        my_lst.pop()
    return my_lst

def deq_popleft():
    for i in range(1):
        my_deq.popleft()
    return my_deq


# extendleft
def lst_extendleft():
    for i in range(1001):
        my_lst.extend([1, 2, 3])
    return my_lst

def deq_extendleft():
    for i in range(1001):
        my_deq.extendleft([1, 2, 3])
    return my_deq


print('-appendleft-')
print('lst', timeit('lst_appendleft()', globals=globals(), number=1000))
print('deq', timeit('deq_appendleft()', globals=globals(), number=1000), '\n')
print('-popleft-')
print('lst', timeit('lst_popleft()', globals=globals(), number=1000))
print('deq', timeit('deq_popleft()', globals=globals(), number=1000), '\n')
print('-extend-')
print('lst', timeit('lst_extendleft()', globals=globals(), number=1000))
print('deq', timeit('deq_extendleft()', globals=globals(), number=1000), '\n')

'''
Резльтат замеров следущий: время выполнения операций очередью намного меньше!
'''


# 3)
def lst_index():
    for i in range(1001):
        my_lst[i] = i
    return my_lst


def deq_index():
    for i in range(1001):
        my_deq[i] = i
    return my_deq


print('-index-')
print('lst', timeit('lst_index()', globals=globals(), number=1000))
print('deq', timeit('deq_index()', globals=globals(), number=1000), '\n')

'''
Резльтат замеров следущий: списко значительно быстрее получает доступ к случайному элементу.
'''

"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit

my_dict = {}
my_ord_dict = OrderedDict()


def append_dict():
    for i in range(1001):
        my_dict[i] = i
    return my_dict


def append_ord_dict():
    for i in range(1001):
        my_ord_dict[i] = i
    return my_ord_dict


print('1')
print('Обычный словарь:', timeit('append_dict()', globals=globals(), number=1000))
print('Упорядоченный словарь:', timeit('append_ord_dict()', globals=globals(), number=1000))

'''
Cоздание обычного словаря быстрее.
'''


def get_dict():
    for key in my_dict:
        my_dict.get(key)
    return my_dict


def get_ord_dict():
    for key in my_ord_dict:
        my_ord_dict.get(key)
    return my_ord_dict


print('2')
print('Обычный словарь:', timeit('get_dict()', globals=globals(), number=1000))
print('Упорядоченный словарь:', timeit('get_ord_dict()', globals=globals(), number=1000))

'''
Возвращения значения ключа у обычного словаря быстрее.
'''


def popitem_dict():
    dict_copy = my_dict.copy()
    for key in range(1001):
        dict_copy.popitem()
    return dict_copy


def popitem_ord_dict():
    ord_dict_copy = my_ord_dict.copy()
    for key in range(1001):
        ord_dict_copy.popitem()
    return ord_dict_copy


print('3')
print('Обычный словарь:', timeit('popitem_dict()', globals=globals(), number=1000))
print('Упорядоченный словарь:', timeit('popitem_ord_dict()', globals=globals(), number=1000))

'''
Удаление последнего элемента у обычного списка на много быстрее!
'''

