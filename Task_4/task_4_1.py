# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]
import math


def get_prime_divisors(number: int):
    """returns a list of prime divisors of a given number"""
    result = []
    for i in range(2, math.ceil(math.sqrt(number))):
        if number % i == 0:
            is_prime = True
            for j in range(2, math.ceil(math.sqrt(i))):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                result.append(i)
    return result


print(get_prime_divisors(600851475143))
