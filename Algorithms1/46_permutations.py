"""
Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 
Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""

class Solution:
    def permute(self, nums):

        #the number of solutions is length(nums)! as all the numbers are unique
        #my solution 
        sol = []
        def swap(a, s): 
            if len(s) == 1: 
                sol.append(a)
                return 

            for i in range(len(s)): 
                aa= a[:]
                ss = s[:]
                aa[s[0]] = a[s[i]]
                aa[s[i]] = a[s[0]]
                x = ss[:i]
                x.extend(ss[i+1:])
                swap(aa,x)
        
        y = [] 
        for i in range(len(nums)):
            y.append(i)
        swap(nums,y)

        return sol 

"""
x = [0,1,2,3,4]
y = x[:]
for i in x:
    z = y[:i]
    z.extend(y[i+1:])
    print(z)
"""
nums = []
x = Solution().permute(nums)
print(len(x), x)

