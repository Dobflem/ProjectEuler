# Multiples of 3 and 5 - Problem 1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
import math


def get_sum(n):
    return (n * (n + 1)) / 2


def solution(max_num):
    three = get_sum(math.floor(max_num/3))
    five = get_sum(math.floor(max_num/3))
    fifteen = get_sum(math.floor(max_num/3))

    print(three + five - fifteen)


solution(1000)
