#!/usr/bin/env python

import itertools

class Solution:
    """
    an O(n) solution
    this does not have the overhead of creating a new sublist
    just to find the sum over and over

    instead it just goes in a linear order and finds the greatest sum
    it takes advantage "contiguous" nature of the problem to solve it
    """

    def maxSubArray(self, nums) -> int:
        sub_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            sub_sum = max(sub_sum + nums[i], nums[i])
            max_sum = max(sub_sum, max_sum)

        return max_sum

class Solution1:
    """
    v1 solution
    slow because basically O(n^2)
    """
    def maxSubArray(self, nums) -> int:
        nl = nums
        cap = len(nl)
        subsum = nl[0]
        maxsum = nl[0]

        for i, n in enumerate(nl): 
            for j in range(i, cap):
                subsum = sum(nl[i:j+1])
                maxsum = max(maxsum, subsum)

        return maxsum


class Solution2:
    """
    v2 solution with itertools
    slow for the same reasons as v1
    """
    def maxSubArray(self, nums) -> int:
        max_sum = nums[0]

        # get list of indexes
        inds = list(range(len(nums)+1))

        # iterate over combinations
        for i, j in itertools.combinations(inds, 2):
            max_sum = max(sum(nums[i:j]), max_sum)
            print(sum(nums[i:j]), nums[i:j])

        return max_sum



s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(s.maxSubArray([-1]))
print(s.maxSubArray([1]))
print(s.maxSubArray([1, 2]))

