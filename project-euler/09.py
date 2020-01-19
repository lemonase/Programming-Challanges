#! /usr/bin/env python3

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def main():
    a = 3
    b = 4
    c = (a**2 * b**2)
    product = a * b * c

    while product != 1000:
        if (a**2 + b**2 != c**2):
            pass
        elif (a**2 + b**2 == c**2):
            product = a * c * b
            print(product)


main()
