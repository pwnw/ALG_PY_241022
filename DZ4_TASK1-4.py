"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры
ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


my_arr = [i for i in range(100)]

print(timeit('func_1(my_arr)', globals=globals(), number=10000))

'''
0.12599929999851156
В данном коде используеть цикл for, с помощью которого перебирается весь массив, и те элементы которые
удовлетворяют условию, записываются в новый массив.
'''


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


"""
Задание 2.
Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение мемоизацией
Сделаны замеры обеих реализаций.
Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!
П.С. задание не такое простое, как кажется
"""
from timeit import timeit
from random import randint
def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'
num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)
print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=10000))
def memoize(f):
    cache = {}
    def decorate(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate
@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'
print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000))

'''
Итоговые замеры:
Не оптимизированная функция recursive_reverse
0.01511820001178421
0.017201900016516447
0.03265209999517538
Оптимизированная функция recursive_reverse_mem
0.001524099992820993
0.0016055000014603138
0.0017867999849840999
Функция вызывается всего 1 раз. Смысла в мемоизации нет.
Время замеров оптимизированной функции гораздо меньше, чем не оптимизированной
т.к словарь был заполнен на первом вызове функции, а во всех остальных
замерах брался уже заполненный.
'''

"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через cProfile и через timeit
Обязательно предложите еще свой вариант решения!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
"""

from timeit import timeit
from cProfile import run

def revers(enter_num, revers_num=0):

def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)
        revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
@@ -35,3 +38,28 @@ def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num
def revers_4(enter_num):
    return ''.join(reversed(str(enter_num)))
enter_num = 1234567890

print('revers_1: ', timeit(f'revers_1({enter_num})', globals=globals()))
print('revers_2: ', timeit(f'revers_2({enter_num})', globals=globals()))
print('revers_3: ', timeit(f'revers_3({enter_num})', globals=globals()))
print('revers_4: ', timeit(f'revers_4({enter_num})', globals=globals()))

run("revers_1(enter_num)")
run("revers_2(enter_num)")
run("revers_3(enter_num)")
run("revers_4(enter_num)")

"""
revers_1:  2.4002221000846475
revers_2:  1.5896976999938488
revers_3:  0.29657999996561557
revers_4:  0.6081014999654144
Третья функция самая быстрая, т.к. отсутсвует арифмитический подсчет
"""


"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1]


@@ -37,5 +39,23 @@ def func_2():
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    a = max(array, key=array.count)
    return f'Чаще всего встречается число {a}, ' \
           f'оно появилось в массиве {array.count(a)} раз(а)'
print(func_1())
print(func_2())
print(func_3())
print("First: " + str(timeit("func_1()", "from __main__ import func_1, array", number=1000)))
print("Second: " + str(timeit("func_2()", "from __main__ import func_2, array", number=1000)))
print("Third: " + str(timeit("func_3()", "from __main__ import func_3, array", number=1000)))

"""
First: 0.0016771000809967518
Second: 0.0041584999999031425
Third: 0.0015302000101655722
Третий вариант самый быстрый
"""

