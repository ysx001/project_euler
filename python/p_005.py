# Project Euler
# Problem 5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def evenly_div(n, m):
	"""
	Find if the posiive integer n is evenly divisidal by all the numbers from 1 to m.

	Args:
	n: the positive integer we are testing
	m: the range of numbers.

	Return:
	A boolean value of whether n is evenly divisible or not.
	"""
	result = True

	for i in range(1, m):
		if n % i != 0:
			result = False
			break

	return result

print(evenly_div(2520, 11))

a = 400000

while not evenly_div(a, 21):
	a += 1

print(a)