# Project Euler
# Problem 6

a = 100

sum_1 = 0
sum_2 = 0

for i in range(1, a+1):
	sum_1 += i**2
	sum_2 += i

sum_2 = sum_2**2

diff = sum_2 - sum_1

print(diff)