"""
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]
 
Constraints:

1 <= s.length <= 12
s consists of lowercase English letters, uppercase English letters, and digits.

"""

class Solution:
    def letterCasePermutation(self, s: str):
        """
        :type S: str
        :rtype: List[str]
        """
        """
        #lets do a depth first search 
        #the tree is a binary tree of the size of the number of letters there are, the  numbers dont matter 
        #and each one has the number of letters squared in possible answers
        sol = [] 
        x = []
        #split all the stings could try and reduce this by including digitis in the steps but not to start with  
        #my method 
        for i in s: x.append(i)
        

        def dfs(remain, next): 

            if len(remain) == 0: 
                sol.append(next)
                return 

            while True: 
                try:
                    int(remain[0]) 
                    y = remain[0]
                    dfs(remain[1:], next+y)
                    break
                except:
                    
                    dfs(remain[1:], next+remain[0].lower())
                    dfs(remain[1:], next+remain[0].upper())
                    break 

        dfs(x, "")
        return sol 
        """

        def backtrack(sub="", i=0):
            if len(sub) == len(s):
                res.append(sub)
            else:
                if s[i].isalpha():
                    backtrack(sub + s[i].swapcase(), i + 1)
                backtrack(sub + s[i], i + 1)
                
        res = []
        backtrack()
        return res


string = "a1b2"
string2 = "1a2b"
string3 = "0"
string4 = "a"

print(Solution().letterCasePermutation(string))