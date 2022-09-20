# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек
# в этой четверти (x и y).

def get_coordinate_range(quarter):
    if quarter == 1:
        print('x > 0 and y > 0')
    elif quarter == 2:
        print('x < 0 and y > 0')
    elif quarter == 3:
        print('x < 0 and y < 0')
    elif quarter == 4:
        print('x > 0 and y < 0')


for i in range(1, 5):
    get_coordinate_range(i)
