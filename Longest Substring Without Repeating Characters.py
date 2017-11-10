"""
Given a string, find the length of the longest substring
without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer
must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        ans = 0
        i = 0
        j = 0
        n = len(s)

        while j < n:
            while j < n and s[j] not in s[i:j]:
                j += 1
            else:
                ans = max(ans, j - i)
                if j < n:
                    i = s[i:j].index(s[j]) + i + 1
        else:
            return ans
