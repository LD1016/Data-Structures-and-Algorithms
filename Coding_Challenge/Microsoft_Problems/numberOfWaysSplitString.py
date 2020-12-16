"""
1573. Number of Ways to Split a String

Given a binary string s (a string consisting only of '0's and '1's), 
we can split s into 3 non-empty strings s1, s2, s3 (s1+ s2+ s3 = s).

Return the number of ways s can be split such that the number of 
characters '1' is the same in s1, s2, and s3.

Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:

Input: s = "10101"
Output: 4
Explanation: There are four ways to split s in 3 parts where each part contain the same number of letters '1'.
"1|010|1"
"1|01|01"
"10|10|1"
"10|1|01"
Example 2:

Input: s = "1001"
Output: 0
Example 3:

Input: s = "0000"
Output: 3
Explanation: There are three ways to split s in 3 parts.
"0|0|00"
"0|00|0"
"00|0|0"
Example 4:

Input: s = "100100010100110"
Output: 12
 

Constraints:

3 <= s.length <= 10^5
s[i] is '0' or '1'.
"""


class Solution(object):
    def numWays(self, s):
        """
        :type s: str
        :rtype: int
        time: n
        space: 1

        """
        mode = 10**9 + 7
        ones = 0
        n = len(s)
        for i in s:
            if i == '1':
                ones += 1
        if ones == 0:
            return int((((n-1)*(n-2))/2) % mode)
        if ones % 3 != 0:
            return 0
        numOnes = ones/3
        window1 = 0
        window2 = 0
        ones = 0
        for i in s:
            if i == '1':
                ones += 1
            if ones == numOnes:
                window1 += 1
            if ones == 2 * numOnes:
                window2 += 1
        return int((window1 * window2) % mode)


test = Solution()
print(test.numWays("10101"))
print(test.numWays("1001"))
print(test.numWays("0000"))
print(test.numWays("100100010100110"))
