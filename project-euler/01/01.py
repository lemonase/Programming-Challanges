#!/usr/bin/env python3

# If we list all the natural numbers below 10 that are multiples of 3 or 5, # we get 3, 5, 6 and 9.
# The total of these multiples is 23.
# Find the total of all the multiples of 3 or 5 below 1000.


def sum_of_multiples(upper):
    total = 0

    for ind in range(upper):
        if ind % 3 == 0:
            total = total + ind
        if ind % 5 == 0:
            total = total + ind

    print("total of multiples:", total)


sum_of_multiples(10)
sum_of_multiples(1000)
