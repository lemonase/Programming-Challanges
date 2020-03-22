#! /usr/bin/env python3

# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

squaresum = 0
nsum = 0

count = 100

for i in range(1, count+1):
    print(i, ': ', i**2)
    nsum += i
    squaresum += i**2

print()
print("nsum =", nsum)
print()
print("nsum squared =", nsum**2)
print("squaresum =", squaresum)
print()
print(nsum**2, "-", squaresum, "=", nsum**2 - squaresum)
