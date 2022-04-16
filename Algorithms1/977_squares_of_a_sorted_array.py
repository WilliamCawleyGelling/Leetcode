"""
Squares Of A Sorted Array 

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

"""


class Solution:
    """
    option one, squring all the inderviduales and then resorting 
    """

    def sortedSquares2(self, nums):
        """ 
        :type nums: list[ints]
        :rtype: list[inrs]
        """
        for i in range(0, len(nums)):
            nums[i] = nums[i]*nums[i]

        nums.sort()
        return nums

    """
    option 2, have outside points and then work from the largest to the smallest
    """
    
    def sortedSquares(self, nums):
        answer = [0] * len(nums)
        l, r = 0, len(nums) - 1
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                answer[r - l] = left * left
                l += 1
            else:
                answer[r - l] = right * right
                r -= 1
        return answer


x = [-10000, -9999, -7, -5]
print(Solution().sortedSquares(x))
