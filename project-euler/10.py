#! /usr/bin/env python3

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# thank you SO https://stackoverflow.com/questions/32542052/sum-of-primes-below-2-000-000-in-python


def sum_primes(end_number):
    start = 3
    end = end_number + 1
    total = 2

    primes = set(range(start, end, 2))

    for num in range(start, end):
        if num not in primes:
            continue

        multiple = num
        while multiple < end:
            multiple += num
            if multiple in primes:
                primes.remove(multiple)

    total += sum(primes)

    return total


# sum_primes(10)
print(sum_primes(2000000))
