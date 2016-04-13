# Problem 3
# Largest prime factor
# https://projecteuler.net/problem=3
#
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

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
    # TODO:0 Make primeFactors more efficient
    r = []
    # Ignore for speed
    # if n%2 == 0:
    #     r.append(2)
    for i in range(1,n/2+1, 2):
        if n%i == 0 and isPrime(i):
            r.append(i)
    return r

# FIXME: Infinite loop?
def largestPrime(n):
    '''Faster version for only the largest prime factor
    Returns number'''
    l = 1
    for i in range(1,n/2+1, 2):
        print l
        if n%i == 0 and isPrime(i):
            l = i
            print l
    return l

# Test
print primeFactors(5)
#>>> []
print primeFactors(10)
#>>> [2,5]
print primeFactors(13195)
#>>> [5, 7, 13, 29]
print primeFactors(12087123)
# print largestPrime(12087123)
#>>> [3, 37, 108893]

# Solution
# print primeFactors(600851475143) # Takes too long
# print largestPrime(600851475143)
