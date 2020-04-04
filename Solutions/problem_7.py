# 10001st prime - Problem 7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#     What is the 10001st prime number?
import math


def is_prime(n, primes):
    for i in range(3, math.ceil(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def solution(n):
    primes = [2, 3, 5, 7, 11, 13]
    total_primes = len(primes)
    number = 15
    while total_primes < n:
        if is_prime(number, primes):
            primes.append(number)
            total_primes += 1
        number += 2
    return primes[-1]


print(solution(10001))
