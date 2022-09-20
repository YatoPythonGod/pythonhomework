# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# *Пример:*
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

from task_2_3 import check_int


def make_bin_to_dec(number: int):
    """converts decimal to binary"""
    dec_lst = []
    while True:
        dec_lst.append(str(number % 2))
        number //= 2
        if number == 0:
            break
    dec_lst.reverse()
    return int(''.join(dec_lst))


print(make_bin_to_dec(check_int()))
print(make_bin_to_dec(25))
