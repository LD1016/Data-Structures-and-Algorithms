"""
Given an 1D integer array A of length N, find the length of longest subsequence 
which is first increasing then decreasing.


Input Format
The first and the only argument contains an integer array A.

Output Format
Return an integer representing the answer as described in the problem statement.

Example Input
Input 1:
 A = [1, 2, 1]
Input 2:
 A = [1, 11, 2, 10, 4, 5, 2, 1]

Example Output
Output 1:
 3
Output 2:
 6


Example Explanation
Explanation 1:
 [1, 2, 1] is the longest subsequence.
Explanation 2:
 [1 2 10 4 2 1] is the longest subsequence.
"""


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestSubsequenceLength(self, A):
        result = 0
        dpA = self.helper(A)
        dpRevA = self.helper(A[::-1])
        dpRevA = dpRevA[::-1]
        for i in range(len(A)):
            result = max(result, dpA[i] + dpRevA[i]-1)
        return result

    def helper(self, A):
        if len(A) <= 1:
            return len(A)
        dp = [1 for i in range(len(A))]
        j, i = 0, 1
        while i < len(A):
            j = 0
            while j < i:
                if A[j] < A[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                j += 1
            i += 1
        return dp


test = Solution()
print(test.longestSubsequenceLength([1, 2, 1]))
print(test.longestSubsequenceLength([1, 11, 2, 10, 4, 5, 2, 1]))
print(test.longestSubsequenceLength([8, 6, 3, 4, 2, 1]))
print(test.longestSubsequenceLength([1, 3, 5, 6, 4, 8, 4, 3, 2, 1]))
