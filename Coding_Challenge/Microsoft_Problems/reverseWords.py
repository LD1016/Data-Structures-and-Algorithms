"""
 Reverse Words in a String

Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. 
The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
Example 4:

Input: s = "  Bob    Loves  Alice   "
Output: "Alice Loves Bob"
Example 5:

Input: s = "Alice does not even like bob"
Output: "bob like even not does Alice"
 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # l = list(s.split())
        # start, end = 0, len(l)-1
        # while start <= end:
        #     l[start], l[end] = l[end], l[start]
        #     start, end = start+1, end-1
        # # return " ".join(l).strip()
        # return " ".join(l)
        return " ".join(reversed(s.split()))


test = Solution()
print(test.reverseWords("the sky is blue"))
print(test.reverseWords("  hello world  "))
print(test.reverseWords("a good   example"))
print(test.reverseWords("  Bob    Loves  Alice   "))
print(test.reverseWords("Alice does not even like bob"))
