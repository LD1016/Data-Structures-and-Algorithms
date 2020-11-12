"""
Problem Description: Given two strings A and B. Find the longest common sequence 
( A sequence which does not need to be contiguous), which is common in both 
the strings.You need to return the length of such longest common subsequence.

Input Format
First argument is an string A.
Second argument is an string B.

Output Format
Return the length of such longest common subsequence between string A and string B.

Example Input
 A = "abbcdgf"
 B = "bbadcgf"

Output: 5

Example Explanation:
 The longest common subsequence is "bbcgf", which has a length of 5
"""


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        a, b = len(A), len(B)
        dp = [[0] * (b+1) for i in range(a+1)]
        result = 0
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                result = max(result, dp[i][j])
        return result


test = Solution()
print(test.solve("abbcdgf", "bbadcgf"))
print(test.solve("bebdeeedaddecebbbbbabebedc", "abaaddaabbedeedeacbcdcaaed"))
