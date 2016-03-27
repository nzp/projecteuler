# Special Pythagorean triplet
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
#
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import itertools


# "When in doubt, use brute force."

for a, b, c in itertools.combinations(range(1, 1001), 3):
    if (a + b + c == 1000) and (a**2 + b**2 == c**2):
        print(a*b*c)
        break
