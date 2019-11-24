#! /usr/bin/env python3

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13. What is the 10,001st prime number?


def main():
    prime_count = 0
    for num in range(1, 1000000000):
        if num > 1:
            for p in range(2, num):
                if num % p == 0:
                    break
            else:
                prime_count += 1
                if prime_count == 6:
                    print(num)
                    break



main()
