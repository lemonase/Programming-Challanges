#! /usr/bin/env python3

# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def isPalindrome(number):
    numList = [int(x) for x in str(number)]
    if len(numList) > 1:
        if numList == list(reversed(numList)):
            return True
    return False


# Brute force FTW \m/
# JK, there are much better ways to solve this
# This works for 3 digits but takes way to long for > 4
def largestPalindromeProduct(num_of_digits):
    numList = [1]

    for n in range(num_of_digits):
        numList.append(0)

    s = [str(n) for n in numList]
    max_value = int("".join(s))

    output = 0
    for i in range(max_value):
        for j in range(max_value):
            product = i * j
            if isPalindrome(product):
                output = product

    print(output)


largestPalindromeProduct(3)

