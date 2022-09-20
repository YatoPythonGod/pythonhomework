# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
#
# *Пример:*
#
# - [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
#  - [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91
from math import floor


# var1
def get_diff_decimal(lst: list):
    """returns the difference between the maximum and minimum values of the fractional part of the elements"""
    new_lst = [float('1.' + str(i).split('.')[1]) for i in lst]
    return round(max(new_lst) - min(new_lst), 2)


# var2(better)
def get_diff_decimal_v2(lst: list):
    """returns the difference between the maximum and minimum values of the fractional part of the elements"""
    new_lst = [i % floor(i) for i in lst]
    return round(max(new_lst) - min(new_lst), 2)


print(get_diff_decimal([1.1, 1.2, 3.1, 5.17, 10.02]))
print(get_diff_decimal_v2([4.07, 5.1, 8.2444, 6.98]))
