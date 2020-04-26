def isPalindromeNumber(n):
	return n == int(str(n)[::-1])

def largestPalindromeProduct(n):
	"""Finds the largest palindrome number made from the product of two n-digit
	numbers.
	"""
	l = list()
	for i in range(10**n-1, 10**(n-1)-1, -1):
		for j in range(i, 10**(n-1)-1, -1):
			l.append(i*j)
	l.sort(reverse=True)
	for n in l:
		if isPalindromeNumber(n):
			return n
	return None

print(isPalindromeNumber(3443))
print(isPalindromeNumber(959))

print(largestPalindromeProduct(3))