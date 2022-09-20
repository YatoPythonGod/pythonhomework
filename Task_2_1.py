# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Учтите, что числа могут быть отрицательными
#
# Пример:
#
# 67.82 -> 23
# 0.56 -> 11

def check_float():
    while True:
        try:
            number = float(input('Please enter a number: '))
            return number
        except ValueError as error:
            print(error)


def sum_num(number):
    result = 0
    for i in str(number):
        if i.isdigit():
            result += int(i)
    return result


print(sum_num(check_float()))
