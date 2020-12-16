"""
1576. Replace All ?'s to Avoid Consecutive Repeating Characters


Given a string s containing only lower case English letters and the '?' character,
convert all the '?' characters into lower case letters such that the final string
does not contain any consecutive repeating characters.
You cannot modify the non '?' characters.
It is guaranteed that there are no consecutive repeating characters in the given
string except for '?'.

Return the final string after all the conversions (possibly zero) have been made.
If there is more than one solution, return any of them. It can be shown that an
answer is always possible with the given constraints.

Example 1:

Input: s = "?zs"
Output: "azs"
Explanation: There are 25 solutions for this problem. From "azs" to "yzs", all are valid. Only "z" is an invalid modification as the string will consist of consecutive repeating characters in "zzs".
Example 2:

Input: s = "ubv?w"
Output: "ubvaw"
Explanation: There are 24 solutions for this problem. Only "v" and "w" are invalid modifications as the strings will consist of consecutive repeating characters in "ubvvw" and "ubvww".
Example 3:

Input: s = "j?qg??b"
Output: "jaqgacb"
Example 4:

Input: s = "??yw?ipkj?"
Output: "acywaipkja"


Constraints:

1 <= s.length <= 100
s contains only lower case English letters and '?'.
"""


class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str

        time: n
        space: 1
        """
        s = [i for i in s]
        for i in range(len(s)):
            if s[i] == '?':
                for j in ['a', 'b', 'c']:
                    if (i > 0 and s[i-1] == j) or (i < len(s)-1 and s[i+1] == j):
                        continue
                    s[i] = j
        return "".join(s)


test = Solution()
print(test.modifyString("ubv?w"))
print(test.modifyString("?zs"))
print(test.modifyString("j?qg??b"))
print(test.modifyString("??yw?ipkj?"))
