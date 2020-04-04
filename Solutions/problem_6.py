# Sum square difference - Problem 6
#
# The sum of the squares of the first ten natural numbers is,
#     (1 ** 2) + (2 ** 2) + ... + (10 ** 2) = 385
#
# The square of the sum of the first ten natural numbers is,
#     (1 + 2 + ... + 10) ** 2 = 55 ** 2 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
#     3025 − 385 = 2640
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum


def solution(n):
    total_sum = 0
    total_s_sum = 0
    for i in range(1, n + 1):
        total_sum += (i ** 2)
        total_s_sum += i
    total_s_sum **= 2
    return total_s_sum - total_sum


print(solution(100))
