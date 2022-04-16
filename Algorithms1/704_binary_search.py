"""
704 Binary Search 
Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:

1 <= nums.length <= 104
-10^4 < nums[i], target < 10^4
All the integers in nums are unique.
nums is sorted in ascending order.


"""

#Lets consider some versions, first a binary search. 
#split the list in the middle and see if the value is above, below or at this point
#continue this until either the number is returned or it is not in the list 
#if not in the list return -1 
#question do we pass the list and the start end index, or do you pass pointers to the list 
#python doesnt pass pythons so i think i would have to pass the whole list everytime (seems very inefficeit)
#this is my first attempt. 
def binary_search(nums, target, low):
    e=len(nums)
    if e == 1 and nums[e-1]!= target:
        return (-1) 
    mid = e//2
    if nums[mid] < target:
        low += mid 
        return binary_search(nums[mid:], target, low)
    elif nums[mid] > target:
        return binary_search(nums[:mid], target, low)
    else:
        return (low + mid)


def search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            return mid
    return -1

ex1 = [-1,0,3,5,9,12]
t1 = 2
p = search(ex1,t1)
print(p)
print("the result of example 1 is ", binary_search(ex1,t1,0))
