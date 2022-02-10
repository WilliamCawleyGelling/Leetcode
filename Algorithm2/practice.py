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


print(1)
a = [1,2,3,4,5,6,7,7,7]
k = 7 
print(Solution.searchRange1(a,a,k))
print(1)
