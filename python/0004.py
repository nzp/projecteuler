# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers
# is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

from itertools import combinations_with_replacement as cwr


def ispalindrome(x):
    y = str(x)

    if y == y[::-1]:
        return True
    else:
        return False

combinations = cwr(range(999, 99, -1), 2)
products = [x * y for x, y in combinations]

print(max([x for x in products if ispalindrome(x)]))
