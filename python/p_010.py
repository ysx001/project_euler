# Project Euler
# Problem 9

from math import *

def sieve_of_eratosthenes(limit):
	primes = [True] * limit
	primes[0] = primes[1] = False
	sum = 0
	
	for (i, is_prime) in enumerate(primes):
		if is_prime:
			for j in xrange(i*i, limit, i):
				primes[j] = False
			sum += i

	return sum

result = sieve_of_eratosthenes(2000000)

print(result)

