# Project Euler
# Problem 4

# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of 

# Find the largest palindrome made from the product of two 3-digit numbers.

# http://articles.leetcode.com/palindrome-number/

# Check is Palindrome for a number by reversing it
# Have the risk of overflow -- but enough for this problem

n = 1000
m = 1000

def isPalindrome(a):
	assert a >= 0
	n = a
	rev = 0
	while a != 0:
		rev = rev * 10 + a % 10
		a /= 10
	return n == rev


print(isPalindrome(9009))

def find_max_palindrome(n, m):
	plist = []
	for i in reversed(range(100, n)):
		for j in reversed(range(100, m)):
			if isPalindrome(i*j):
				plist.append(i*j)
	result = max(plist)
	return result	

result = find_max_palindrome(n,m)

print(result)