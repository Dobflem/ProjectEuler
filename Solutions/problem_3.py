# Largest prime factor - Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
import math


def solution(max_num):
    sqrt = int(math.sqrt(max_num))
    primes = [3, 5]
    largest_factor = 0

    for i in range(7, sqrt, 2):
        prime = True
        max_for_i = int(math.sqrt(i))

        for j in primes:
            if j > max_for_i:
                break

            if i % j == 0:
                prime = False
                break

        if prime:
            primes.append(i)
            if max_num % i == 0:
                largest_factor = i

    print(largest_factor)


solution(600851475143)
