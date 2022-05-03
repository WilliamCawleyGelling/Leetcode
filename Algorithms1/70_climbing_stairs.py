"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 
Constraints:

1 <= n <= 45
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        :type n: int 
        :rtype: int 
        """

        #can take 1 or 2 steps at a time up until the 
        #i have two approaches to this 
        #1. is a depth first search approach
        #with a left hand heavy tree 
        #approach two takes advantage that the largest array can be is n
        #and the smallest it can be is (1+n)//2 (floored, add one so it is the same as doing upper instead of floor)

        #on reflection it is the fibbonachi sequence so 

        if n == 0: return 0 
        if n == 1: return 1
        if n == 2: return 2 

        x = 1
        y = 2 
        
        for _ in range(n-2):
            total = y + x
            x = y
            y = total
        return total 
            
print(Solution().climbStairs(10))
        

