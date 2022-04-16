"""
Given an integer array nums, move all 0's to the end of it while maintaining 
the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1
 

Follow up: Could you minimize the total number of operations done?

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        Do not return anything, modify nums in-place instead.
        
"""

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums:List[int]
        :rtype :none
        Do not return anything, modify nums in-place instead.
        """
        i = 0 
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        print(nums)

Solution().moveZeroes([0,1,0,3,12])



