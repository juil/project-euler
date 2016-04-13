# Problem 3
# Largest prime factor
# https://projecteuler.net/problem=3
#
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
import math
def isPrime(n):
    '''Check if n is a prime number
    Take number n as input
    Return boolean'''
    if n in [0, 1]:
        return False
    for i in range(3,n/2):
        if n%i == 0:
            return False
    return True

# Test
for i in range(10):
    print i, isPrime(i)

def primeFactors(n):
    '''List all prime factors of n
    Takes number n as input
    Returns a list of numbers'''
    r = []
    if n%2 == 0:
        r.append(2)
    for i in range(1, n/2+1, 2):
        if n%i == 0 and isPrime(i):
            r.append(i)
    return r

# DONE:0 Fix looping problem
def largestPrime(n):
    '''Faster version for only the largest prime factor
    Returns number

    Start by going backwards from largest factor '''
    largest = 0
    for i in range(1, int(math.sqrt(n)/2)):
        if n%i == 0:
            if isPrime(n/i):
                return n/i
            # elif isPrime(i): #comment out for speed
            #     largest = i
    return largest

    # Slow method
    # l = 1
    # for i in range(1, n/2+1, 2):
    #     if n%i == 0 and isPrime(i):
    #         l = i
    # return l

# Test
print primeFactors(5)
#>>> []
print primeFactors(10)
#>>> [2,5]
t=13195
print "Find:", t
print primeFactors(t)
print largestPrime(t)
#>>> [5, 7, 13, 29]
t=12087123
print "Find:", t
print primeFactors(t)
print largestPrime(t)
#>>> [3, 37, 108893]
t=1208712371
print "Find:", t
# print primeFactors(t)
print largestPrime(t)
#>>>

# Solution
s = 600851475143
# print primeFactors(s) # Takes too long
# print largestPrime(s)
