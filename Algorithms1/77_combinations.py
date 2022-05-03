"""
Given two integers n and k, return all possible combinations of k 
numbers out of the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
1 <= k <= n
"""

class Solution:
    def combine(self, n: int, k: int):
      #this doesnt need all combinations in every position just the combinations 
        
      sol = [] 
        
      def backtracking(remain, comb, next): 
          #if a solution is found, condition of k is met 
          if remain == 0: 
            sol.append(comb[:])
          else: 
            #iterate through all possible candidates 
            for i in range(next, n+1): 
              #add a candidate 
              comb.append(i)
              #backtrack 
              backtracking(remain-1, comb, i+1)
              #remove candidate 
              comb.pop()


      backtracking(k,[],1)
      return sol 




print(Solution().combine(4,3))