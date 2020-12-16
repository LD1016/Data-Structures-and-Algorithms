"""
266. Palindrome Permutation

Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
"""


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hashMap = {}
        for i in s:
            if i in hashMap.keys():
                hashMap[i] += 1
            else:
                hashMap[i] = 1
        odds = 0
        for v in hashMap.values():
            if v % 2 != 0:
                odds += 1
        return True if odds <= 1 else False


test = Solution()
print(test.canPermutePalindrome("code"))
print(test.canPermutePalindrome("aab"))
print(test.canPermutePalindrome("carerac"))
