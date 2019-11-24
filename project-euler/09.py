#! /usr/bin/env python3

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
