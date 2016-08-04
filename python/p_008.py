# Project Euler
# Problem 8


f = open('p_8.txt', 'r')
string = f.read()

n = len(string)

num_list = [0] * n



for i in range(n):
	num_list[i] = int(string[i])

a = 13

product_list = [1] * (n-a)

for i in range(n-a):
	for j in range(a):
		product_list[i] *= num_list[i+j]

print(product_list)

result = max(product_list)

print(result)
