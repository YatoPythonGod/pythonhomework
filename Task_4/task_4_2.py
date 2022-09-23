# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной
# последовательности. Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4] -

# *** кажется, неправильный пример, поскольку нам нужно получить список неповторяющихся элементов Исходной
# последовательности, т.е --> [1,1,1,1,2,2,2,3,3,3,4] -> [4] т.к 4 не повторяется в исходном списке


def unique_numbers(lst: list):
    """returns a list of non-repeating elements of the source list"""
    repeat_num = set()  # использую множество для оптимизации алгоритма, а не для решения задачи
    unique_num = set()
    for number in lst:
        if number in repeat_num:
            continue
        elif number in unique_num:
            unique_num.remove(number)
            repeat_num.add(number)
            continue
        unique_num.add(number)
    return list(unique_num)


print(unique_numbers([1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 10, 11, 11]))
