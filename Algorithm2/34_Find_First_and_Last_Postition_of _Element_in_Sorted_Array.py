"""
solution to the following problem with multiple possible solutions
Search range: given an array nums sorted in non decreasing order,
Find the starting and ending postion of a given target value 

if target is not found in the array, return [-1,-1]. 

must be written with O(log(n)) runtime complexity

input: 
nums - list of intergers
target - integer targer 

output: 
out - in the form [x,y] where x=start and y= end. If not found then return [-1,-1]
"""

class Solution:

    #First solution, using initial thoughts
    #find the output by scrolling across the array from left to right
    #if it finds target it then searches from right to left. 
    def searchRange1(self, nums, target):
        x = -1
        y = -1
        length = len(nums)
        for i in range(0, length): 
            if nums[i] == target:
                x = i
                while (i+1 < length) and (nums[i+1] == target): 
                    i += 1 
                y = i 
                break 
        return [x,y]

    #use nums.index(target) to find list and then searches
    
    def searchRange2(self, nums, target):
        length = len(nums)
        if length > 0 and target < nums[0] and target > nums[length-1]:
            return [-1,-1]
        try: 
            x = nums.index(target)
        except:
            return [-1,-1]
        i = x+1
        while (i < length) and (nums[i] == target):
            i+=1
        return([x,i-1])

    #using binary search left and right 
    #method taken from comments by richme in discussion. 
    #is slower on the tests, argument for binary search vs inbuilt search method.
    def searchRange3(self, nums, target):
        def binarySearchFindPos(nums, target, find_start: bool=True):
            low, high, res = 0, len(nums) - 1, -1
            while(low <= high):
                mid = (low + high) // 2
                if nums[mid] == target:
                    res = mid
                    if find_start:
                        high = mid - 1
                    else:
                        low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
            return res
        
        start = binarySearchFindPos(nums, target)
        end = binarySearchFindPos(nums, target, False)
        return [start, end]




    