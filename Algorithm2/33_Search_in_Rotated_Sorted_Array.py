"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, 
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

constraints are 
1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^
nums is an ascending array that is possibly rotated.
-10^4 <= target <= 10^4


"""

class Solution:

    #first nieve approach
    #if you just search along linearly for the target and if its there return the index point
    #this is a O(n) solution  
    def search(self, nums, target):

        for i in range(0,len(nums)):
            if nums[i] == target: 
                return i 
        return -1

    #I am looking for a log(n) solution, this will require dividing code and looking if code is above or below 
    #look at start point 
    #look at end point 
    #look at mid point 
    #if mid point is bigger then start point then shift is after 
    #if mid point is smaller then start point then shift is before 
    #depending on if target is bigger or smaller then midpoint depends on where it goes 
    #call itself back again on half the size 


    def search(self, nums, target):
        n = len(nums)
        left, right = 0, n - 1
        if n == 0: return -1
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target: return mid
            
            # inflection point to the right. Left is strictly increasing
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            # inflection point to the left of me. Right is strictly increasing
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1
            
        




    

#demo example 
nums = [4,5,6,7,0,1,2]
target = 2
print(Solution.search(nums, nums, target))