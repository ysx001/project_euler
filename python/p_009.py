# Project Euler
# Problem 9

for a in range(1, 1000):
	for b in range(a, (1000-a)):
		c = 1000 - (a+b)
		x = a**2 + b**2
		y = c**2
		if x == y:
			print (a,b,c)
			print (a*b*c)
			break

 

