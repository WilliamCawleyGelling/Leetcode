"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.

"""

class Solution:
    def singleNumber(self, nums) -> int:
        """
        :type nums: list[int]
        :rtype: int 
        """
        """
        #in constant extra space that could be an array that is popped in and out of when one is met, and removed when found again 
        #could make a dictionary 
        
        #using sorting sorting

        if len(nums) == 1: 
            return nums[0]  
        nums.sort() 
        for i in range(0, len(nums)-1,2): 
            if nums[i] != nums[i+1]: 
                return nums[i]

        return nums[-1]
        """

        #option two uses xor bit manipulation 
        #this takes addvantage that the sum of the same two numbers always gives zero so whats left is the remaining number 
        
        xor = 0
        for num in nums:
            xor ^= num
        
        return xor

            
print(Solution().singleNumber([4,1,2,1,2]))            
            


            
