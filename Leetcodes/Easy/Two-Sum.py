# Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

from typing import Any


def twoSum(nums, target):
    seen = {}  # value -> index
    
    for i, num in enumerate(nums):
        missing_number = target - num
        if missing_number in seen:
            return [seen[missing_number], i]
        seen[num] = i



print(twoSum([2,7,11,15], 13))