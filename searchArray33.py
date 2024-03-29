'''
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''

# My original Python solution beats 11%
class Solution(object):
    def search(self, nums, target):
        count = 0 
        for n in nums:
            if n == target:
                return count
            else:
                count+=1
        return -1

# With research use enumerate, beats 65%:
class Solution(object):
    def search(self, nums, target):
        for count, n in enumerate(nums):
            if n == target:
                return count
        return -1
