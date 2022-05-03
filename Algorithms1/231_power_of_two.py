"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false
 

Constraints:

-231 <= n <= 231 - 1
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        #bin is the binary function 
        #&is the bitwise add 
        #if divisble by two is off the form 10000.. 
        #n-1 then is of the form 1111... with one less length, add them together and you get 0 
        if n == 0: return False
        if  n & n-1 == 0: return True
        else: return False 

print(Solution().isPowerOfTwo(8))