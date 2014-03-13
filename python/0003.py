# Largest prime factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

import math


def prime_sieve(limit):
    '''Sieve of Eratosthenes.

    '''
    numlist = [True] * limit
    numlist[0] = numlist[1] = False

    for (p, isprime) in enumerate(numlist):
        if isprime:
            yield p
            for i in range(p**2, limit, p):
                numlist[i] = False


n = 600851475143  
factor_limit = math.ceil(math.sqrt(n))
primes = prime_sieve(factor_limit)

# Simple trial division.
for f in primes:
    if n % f == 0:
        max_f = f 
        n /= f
if n > 1:
    max_f = n

print("The largest factor is %d." % max_f)
