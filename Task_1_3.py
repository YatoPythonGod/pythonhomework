# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

def get_quarter(x, y):
    if x > 0:
        if y > 0:
            print('I')
        else:
            print('IV')
    else:
        if y > 0:
            print('II')
        else:
            print('III')


get_quarter(-10, 10)