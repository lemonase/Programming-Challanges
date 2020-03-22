#! /usr/bin/env python3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


def gpf(num):
    factors = []
    i = 2

    while i <= num:
        if i in factors:
            continue

        if num % i == 0:
            factors.append(i)
            num = num / i

        i += 1

    return factors


print(gpf(13195)[-1])
print(gpf(600851475143)[-1])
