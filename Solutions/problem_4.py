# Largest palindrome product - Problem 4
#
#
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
import math


def memoize(f):
    memo = {}

    def wrapper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return wrapper


@memoize
def is_palindrome(val):
    val_s = str(val)
    return val_s == val_s[::-1]


def solution():
    count = 100
    max_count = (count * 10) - 1
    max_num = 0

    i = max_count
    while i > count - 1:
        for j in range(max_count, count - 1, -1):
            val = i * j
            if val > max_num:
                if is_palindrome(val):
                    count = int(math.sqrt(val))
                    max_num = val
                    break
        i -= 1

    print(max_num)


solution()
