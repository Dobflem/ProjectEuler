# Special Pythagorean triplet - Problem 9
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#     (a ** 2) + (b ** 2) = (c ** 2)
#
# For example, (3 ** 2) + (4 ** 2) = 9 + 16 = 25 = (5 ** 2).
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import math


def solution(n):
    sqrs_d = {k**2: k for k in range(1, n)}
    sqrs_l = list(sqrs_d.keys())

    for i in range(len(sqrs_l) - 1, -1, -1):
        c_sqrd = sqrs_l[i]
        for j in range(math.ceil(math.sqrt(c_sqrd))):
            a_sqrd = sqrs_l[j]
            b_sqrd = c_sqrd - a_sqrd
            if b_sqrd in sqrs_d:
                a = sqrs_d[a_sqrd]
                b = sqrs_d[b_sqrd]
                c = sqrs_d[c_sqrd]
                if a + b + c == 1000:
                    return a * b * c
    return None


print(solution(1000))
