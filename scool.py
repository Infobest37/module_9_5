#####################Пример номер -1 библиотека iterators#########################
'''Показывает как работать с интераторами и как интераторы экономят память'''

import sys
from itertools import repeat
ex_itertator = repeat( "4", 100_000)
print(ex_itertator)
print(f"Размер итератора - {sys.getsizeof(ex_itertator)}")

ex_str = "4" * 100_000
print(f"Размер итератора - {sys.getsizeof(ex_str)}")
print("##############################################################################")
#####################Пример №2 - работа итераторов в классе#############################
'''В этом примере будем разберать работу интераторов в классе'''
class Iter:
    def __init__(self):
        self.first = "Первый элемент"
        self.second = "Второй элемент"
        self.third = "Третий элемент"
        self.i = 0

    def __iter__(self):
        # обнуляем счетчик перед циклом
        self.i = 0
        # возращаем ссылку на себя, так как сам объект должен быть итератором
        return self

    def __next__(self):
        # этот метод возвращает значение по требованию python (ленивые вычисления)
        self.i += 1
        if self.i == 1:
            return self.first
        if self.i == 2:
            return self.second
        if self.i == 3:
            return self.third
        if self.i == 4:
            return "Подсчет закончил"
        raise StopIteration # Признак того что больше вызывать нечего

obj = Iter()
# print(obj)
# # print(next(obj))
#
# for i in obj:
#     print(i)
try:
    while True:
        val = obj.__next__()
        print(val)
except StopIteration:
    pass

# То есть интерератор вызывает метод __next__  каждом переходе цикла
# Если в __next__ возникают исключения StopIteration - то значит в объекте нет больше элементов,
# цикл прекращается
print("##############################################################################")
#####################Пример №3 - функция фебоначе через функцию фор #############################

# def fibonacci(n):
#     result = []
#     a, b = 0, 1
#     for _ in range(n):
#         result.append(b)
#         a, b = b, a + b
#     return result
''' Если мы захотим как напечатать все наши значения «fibonacci», которые у нас здесь возвращаются, 
нам придётся все сохранить в список «result», потом вернуть этот список. Ещё потом нужно прогнаться 
циклом «for»'''
# for i in fibonacci(n = 10):
#     print(i)
'''Все работает. Но даже такие маленькие вычисления уже намного больше времени занимают, нежели если бы это
 был наш собственный итератор.'''
print("##############################################################################")
#####################Пример №4 - функция фебоначе через класс #############################
print("##############################################################################")

class Fibonacci:
    def __init__(self, n):
        self.i, self.a, self.b,  self.n = 0, 0, 1, n

    def __iter__(self):
        self.i, self.a, self.b = 0, 0, 1
        return self
    def __next__(self):
        self.i += 1
        if self.i >= 1:
            if self.i > self.n:
                raise StopIteration()
            self.a, self.b = self.b, self.a + self.b
        return self.a
fib_iter = Fibonacci(10)
print(next(fib_iter))

for i in fib_iter:
    print(i)



