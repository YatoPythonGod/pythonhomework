# Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)

import time


def my_random(start, end):
    random_number = int(str(time.time()).rsplit('.')[1])
    return random_number % (end - start) + start


print(my_random(1, 100))
print(my_random(600000, 1000000))
