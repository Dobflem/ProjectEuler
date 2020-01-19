# Largest palindrome product - Problem 4
#
#
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.


def solution():
    max_num = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            val = i * j
            val_s = str(val)
            if val_s == val_s[::-1]:
                if val > max_num:
                    max_num = val
    print(max_num)


solution()
