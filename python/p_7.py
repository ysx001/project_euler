# Project Euler
# Problem 7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.

# What is the 10 001st prime number?

# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

from math import *

def sieve_of_eratosthenes(nth, limit = 10000000):
	prime_count = 0
	primes = [True] * limit
	primes[0] = primes[1] = False

	for (i, is_prime) in enumerate(primes):
		 if is_prime:
		 	prime_count += 1
		 	for j in xrange(i*i, limit, i):
		 		primes[j] = False
		 	if prime_count == nth:
		 		prime = i
		 		break
	return prime

print(sieve_of_eratosthenes(10001))
