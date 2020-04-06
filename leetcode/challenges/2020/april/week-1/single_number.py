#!/usr/bin/env python

from collections import Counter

class Solution:
    def singleNumber(self, nums) -> int:
        num_counter = Counter(nums)
        for k, v in num_counter.items():
            if v == 1:
                print(k)


s = Solution()
s.singleNumber([2, 2, 5, 5, 4])
s.singleNumber([2, 2, 1])

