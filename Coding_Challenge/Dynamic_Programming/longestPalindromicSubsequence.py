"""
Problem Description: Given a string A, find the common palindromic sequence 
( A sequence which does not need to be contiguous and is a pallindrome), which is common in itself.
You need to return the length of longest palindromic subsequence in A.

Example Input:
 A = "bebeeed"

Example Output:
 4
"""


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        dp = [[0]*(n) for i in range(n)]
        for i in range(len(dp)):
            dp[i][i] = 1
        for l in range(2, len(dp) + 1):
            for i in range(0, len(dp)-l + 1):
                j = l + i - 1
                if A[i] == A[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        return dp[0][n-1]


test = Solution()
print(test.solve("bebeeed"))
print(test.solve("bebdeeedaddecebbbbbabebedc"))
