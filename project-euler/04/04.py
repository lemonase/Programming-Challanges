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


def largestPalindromeProduct(num_of_digits):
    max_value = 10 ** num_of_digits

    for i in range(max_value, 0, -1):
        for j in range(max_value, 0, -1):
            product = i * j
            if isPalindrome(product):
                return product


print(largestPalindromeProduct(3))
