"""
Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

Example 3:

Input: s = "a"
Output: "a"

Example 4:

Input: s = "ac"
Output: "a"
 
Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),

"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        end = 0
        maxLen = 0
        for i in range(len(s)):
            case1 = self.longestFromMiddle(s, i, i)
            case2 = self.longestFromMiddle(s, i, i+1)
            maxLen = max(case1, case2)
            if maxLen > end - start:
                start = i - ((maxLen-1)//2)
                end = i + (maxLen//2)
        return s[start:end+1]

    def longestFromMiddle(self, s, left, right):
        while left >= 0 and right < len(s) and left <= right and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1


test = Solution()
print(test.longestPalindrome("babad"))
print(test.longestPalindrome("cbbd"))
print(test.longestPalindrome("a"))
print(test.longestPalindrome("ac"))
