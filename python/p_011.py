# Project Euler
# Problem 11

with open('p_011.txt') as f:
	num_list = [map(int, line.split()) for line in f]


hoz_product = [0] * 20
ver_product = [0] * 20

def max_product(alist, num_adj):
	n = len(alist)
	a = num_adj
	product_list = [1] * (n-a)
	for i in range(n-a):
		for j in range(a):
			product_list[i] *= alist[i+j]

	return max(product_list)

trans_num_list = [list(i) for i in zip(*num_list)]

for i in range(20):
	hoz_product[i] = max_product(num_list[i], 4)
	ver_product[i] = max_product(trans_num_list[i], 4)

print('horizontal product: ', max(hoz_product))
print('vertical product: ', max(ver_product))


def diag_max(alist, num_adj):

	n = len(alist[0])
	a = num_adj

	diag_product = [1] * (n-a)

	for i in range(n-a):
		for j in range(a):
			diag_product[i] *= num_list[j][i+j]

	return max(diag_product)

diag_product_l = [0] * 16
diag_product_r = [0] * 16

for i in range(16):
	diag_product_l[i] = diag_max(num_list[i:i+4], 4)
	diag_product_r[i] = diag_max(num_list[i:i+4][::-1], 4)


print(diag_product_l)
print(diag_product_r)




