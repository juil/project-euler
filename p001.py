# Problem 1
# Multiples of 3 and 5
#
# Find the sum of all multiples of 3 or 5 below 1000.

def sum3or5(max):
    sum = 0
    for i in range(max):
        if i%3==0 or i%5==0:
            sum += i

    return sum

# Test Cases
print sum3or5(10)
print sum3or5(1000)
