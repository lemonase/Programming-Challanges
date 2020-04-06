# Leetcode April 30day Challenge

## Week 1 (April 1st - April 7th)

### 1. Single Number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

```
Example 1:

Input: [2,2,1]
Output: 1

Example 2:

Input: [4,1,2,1,2]
Output: 4
```

### 2. Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:
```
Input: 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
```

### 3. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

```
Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
```

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


### 4. Move Zeros

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

```
Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
```

Note:

    You must do this in-place without making a copy of the array.
        Minimize the total number of operations.


