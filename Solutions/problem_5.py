# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def get_minimum_divided(a, b):
    dividers = [a, b]
    max_divider = max(dividers)
    num = 0
    found = False
    while not found:
        num += max_divider
        found = True
        for divider in dividers:
            if num % divider != 0:
                found = False
                break
    return num


def half_dividers(arr):
    dividers = []

    while arr:
        x = arr.pop(0)
        try:
            y = arr.pop(0)
            dividers.append(get_minimum_divided(x, y))
        except IndexError:
            dividers.append(x)

    return dividers


def solution():
    num_range = 20
    dividers = [i for i in range(num_range, 0, -1)]

    # Divide and Conquer
    while len(dividers) > 1:
        dividers = half_dividers(dividers)

    print(dividers[0])


solution()
