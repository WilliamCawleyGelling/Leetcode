"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, 
or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        """
        :type s1: str
        :type s2: str 
        :rtype: bool
        """

        if not s1 and s2: 
            return False
        if  len(s1) > len(s2): 
            return False
        #now we need to consider if it containes a permutation of the string 
        #look at a sliding window of size s1,
        #if this window containes the same values then its true
        #could make them both into dictionarys with values and then check if they exist in value 
        #split the string s1 into a a dictionary 

        #could generate them both with a dict with just lowercase english letters 
        """
        dicts1 = {}
        for i in s1.split(""): 
            if i in dicts1:
                dicts1[i] += 1
            else: 
                dicts1[i] = 1

        dicts2 = {}
        for i in s2[:len(s1)-1]:
            if i in dicts2:
                dicts2[i] += 1
            else: 
                dicts2[i] = 1
        """
        alphabet = 'qwertyuiopasdfghjklzxcvbnm'
        dicts1, dicts2 = {}, {} 
        #initalize empty dictionarys for use 
        start, end = 0, len(s1)

        for i in alphabet: 
            dicts1[i] = 0 
            dicts2[i] = 0

        for letter in s1: 
            dicts1[letter] += 1 

        for letter in s2[:end]:
            dicts2[letter] += 1
        
        while end <= len(s2): 
            #check if they match 
            if dicts1 == dicts2: 
                return s2[start:end]
            #printing the dictionarys 
            
            print("this is dicts1: ")
            for k, v in dicts1.items(): 
                print(k,v)
            print("this is dicts2: ")
            for k, v in dicts2.items(): 
                print(k,v)
            
            if end < len(s2):
                dicts2[s2[start]] -= 1 
                dicts2[s2[end]] += 1
            end += 1
            start += 1

        return False

        

#s1 = "ab"
#s2 = "eidbaooo"

#example 2 
s1 = "ab" 
s2 = "eidboaoo"

#s1 = "a"
#s2 = "bcda"
print(Solution().checkInclusion(s1,s2))        