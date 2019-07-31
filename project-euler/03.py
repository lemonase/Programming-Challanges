#! /usr/bin/env python3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


def get_prime_factors(num):
    """
    Returns a list of factors for a given number
    """
    prime_set = set()

    for ind in range(2, num):
        if num % ind == 0:
            if len(get_prime_factors(ind)) == 0:
                prime_set.add(ind)

    return prime_set


def get_largest_prime_factor(num):
    i = 2
    while i**2 < num:
        if num % i:
            i += 1
        else:
            num //= i

    return num

print(sorted(get_prime_factors(13195)))
print(get_largest_prime_factor(13195))
# print(sorted(get_factors(600851475143)))



