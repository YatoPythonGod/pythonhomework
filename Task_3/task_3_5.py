# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи](https://clck.ru/yWbkX.)

def get_fib(count: int):
    """returns a list of fibonacci sequence"""
    fib1 = 0
    fib2 = 1
    fib_lst = []
    for i in range(count):
        fib_lst.append(fib2)
        fib1 += fib2
        fib1, fib2 = fib2, fib1
    return fib_lst


def get_negafib(count: int):
    """returns a list of negafibonacci sequence"""
    fib1 = 0
    fib2 = 1
    fib_lst = []
    for i in range(1, count + 1):
        fib_lst.append(fib2 * pow(-1, i + 1))
        fib1 += fib2
        fib1, fib2 = fib2, fib1
    return fib_lst


def get_all_fib(count: int):
    """returns a list of negafibonacci plus fibonacci sequence"""
    result = list(reversed(get_negafib(count)))
    result.append(0)
    result.extend(get_fib(count))
    return result


print(get_fib(8))
print(get_negafib(8))
print(get_all_fib(8))
