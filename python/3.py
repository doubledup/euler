#What is the largest prime factor of the number 600851475143?
import math


def isPrime(num):
    if num % 2 == 0:
        return False
    for i in [x for x in range(3, math.floor(math.sqrt(num)) + 1) if x % 2 == 1]:
        if num % i == 0:
            return False
    return True

def biggestPrime(num):
    """Finds the biggest prime number that divides num"""
    if isPrime(num):
        return num
    else:
        y = num
        # Deal with factors of 2
        if y % 2 == 0:
            while y % 2 == 0:
                mPrime = 2
                y //= 2
                # print(y)
        else:
            mPrime = 1

        # Divide out all primes <= sqrt(num)
        for i in range(3, math.floor(math.sqrt(num)) + 1, 2):
            while y % i == 0 and isPrime(i):
                mPrime = i
                # print('found', mPrime)
                y //= i

        # If the max prime occurred only once, it hasn't been divided out yet
        if y > 1 and isPrime(y):
            return y
        # Else the max prime is the last prime found
        else:
            return mPrime

print('biggest prime:', biggestPrime(600851475143))
print('biggest prime:', biggestPrime(7))
print('biggest prime:', biggestPrime(22))
print('biggest prime:', biggestPrime(9))
print('biggest prime:', biggestPrime(128))
print('biggest prime:', biggestPrime(27))

