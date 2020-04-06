#!/usr/bin/env python

class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zc = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zc += 1

        for i in range(zc):
            nums.remove(0)
            nums.append(0)

        print(nums)


s = Solution()
s.moveZeroes([0, 1, 0, 3, 12])
s.moveZeroes([0, 0, 1])
