# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def get_length():
    ax, ay = map(float, input('Please enter the coordinates of point A: ').split(','))
    bx, by = map(float, input('Please enter the coordinates of point B: ').split(','))
    return round(((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5, 2)


print(get_length())
