class StepValueError(ValueError):
    pass
class ValueError(Exception):
    pass

class Iterator:
    def __init__(self, start, stop : int, step = 1):
        self.start = start
        self.stop = stop
        self.step = step
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0')
    def __iter__(self):
        self.pointer = self.start
        return self
    def __next__(self):
        result = self.pointer  # сохраняет первое значение перед увеличением шага

        if self.step > 0:
            self.pointer += self.step
            if self.pointer > self.stop + 1:
                raise StopIteration
        if self.step < 0:
            self.pointer += self.step
            if self.pointer < self.stop - 1:
                raise StopIteration
        return result # сохраняет текущее значение

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()
