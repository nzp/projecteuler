# 10001st prime
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
#
# What is the 10 001st prime number?

# From the prime number theorem we estimate the number and double it for good
# measure.  So, n * ln(n) ~ 92114 and times two:

limit = 184227

count = 0

# And then we just sieve through.

a = [True] * limit
a[0] = a[1] = False

for (i, isprime) in enumerate(a):
    if isprime:
        count += 1
        if count == 10001:
            print(i)
            break

        for n in range(i**2, limit, i):
            a[n] = False

