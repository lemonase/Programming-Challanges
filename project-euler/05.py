#! /usr/bin/env python3
# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of
# the numbers from 1 to 20?

def evenlyDivisible(input_num):
    for i in range(2, 20):
        if input_num % i != 0:
            return False

    return True


def smallestMultiple():
    i = 2
    while not evenlyDivisible(i):
        i += 2

    print(i)


smallestMultiple()
