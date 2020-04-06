#!/usr/bin/env python
import sys


class Solution:
    def isHappy(self, n: int) -> bool:
        nn = n
        visited = set()

        while True:
            # (re)set sum to 0
            pow_sum = 0

            # convert num into a list of num
            nl = [int(x) for x in str(nn)]

            # sum up all the powers
            pow_sum = sum([pow(num, 2) for num in nl])

            # exit if sum is one
            if pow_sum == 1:
                return True

            # if sum has repeated, not a happy number
            if pow_sum in visited:
                return False

            # add sum to list of visited numbers
            visited.add(nn)

            # set next input to the sum
            nn = pow_sum


s = Solution()
print(s.isHappy(19))
print(s.isHappy(2))
