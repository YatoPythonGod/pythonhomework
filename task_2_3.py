# Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.

def check_int():
    """checks that the input is a number"""
    while True:
        try:
            number = int(input('Please enter a number: '))
            return number
        except ValueError as error:
            print(error)


def get_palindrome(num):
    result = num
    while str(result) != str(result)[::-1]:
        result = result + int(str(result)[::-1])
    return result


if __name__ == '__main__':
    print(get_palindrome(check_int()))
