"""
Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "ababccbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if len(s) == 1:
            return 1
        max_len = 1
        start = 0
        end = 1
        while end < len(s):
            if s[end] in s[start:end]:
                max_len = max(max_len, end - start)
                start = s[start:end].index(s[end]) + 1
            end += 1
        max_len = max(max_len, end - start)
        return max_len
    # how best to do this
    # length of longest substring
    # idea one, two pointers
    # and a string, if it is in the current subs string then sub string ends

    def lengthOfLongestSubstring2(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # if not s, saying if s doesnt exist then return 0
        if not s:
            return 0
        # if len(s) == 1 then can just return 1
        if len(s) == 1:
            return 1
        max_len = 1
        start = 0
        end = 1
        while end < len(s):
            #print(start, end, s[start:end], s[end])
            if s[end] in s[start:end]:  # when an repition has occured
                # print([s[end]])
                # decide if its bigger then previouse maximum
                max_len = max(max_len, end - start)
                # find index position of the first letter that has been repeated and move start to step after. do this by doing start ++
                start += s[start:end].index(s[end])+1
                #print("start = ", start)
            end += 1
        max_len = max(max_len, end - start)
        return max_len

    def lengthOfLongestSubstring3(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans


print(Solution().lengthOfLongestSubstring3("ababccbb"), "expected 3")  # 3
print(Solution().lengthOfLongestSubstring3("bbbbb"), "expected 1")  # 1
print(Solution().lengthOfLongestSubstring3("pwwkew"), "expected 3")  # 3
