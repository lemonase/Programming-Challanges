#! /usr/bin/env python3
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def smallestMultiple(small):
    i = 1
    while i < 21:
        while small % i != 0:
            small += 1
            i = 1
        i += 1

    print(small)


smallestMultiple(1)
