"""
Find the longest increasing subsequence of a given array of integers, A.
In other words, find a subsequence of array in which the subsequence’s elements
are in strictly increasing order, and in which the subsequence is as long as possible.
This subsequence is not necessarily contiguous, or unique.
In this case, we only care about the length of the longest increasing subsequence.


Input 1:
    A = [1, 2, 1, 5]

Output 1:
    3

Explanation 1:
    The sequence : [1, 2, 5]

Input 2:
    A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

Output 2:
    6

Explanation 2:
    The sequence : [0, 2, 6, 9, 13, 15] or [0, 4, 6, 9, 11, 15] or [0, 4, 6, 9, 13, 15]
"""


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        if len(A) <= 1:
            return len(A)
        dp = [1 for i in range(len(A))]
        ac = [i for i in range(len(A))]
        j, i = 0, 1
        while i < len(A):
            j = 0
            while j < i:
                if A[j] < A[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        # set the actualSolution to point to guy before me
                        ac[i] = j
                j += 1
            i += 1
        return max(dp)


test = Solution()
print(test.lis([1, 2, 1, 5]))
print(test.lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
print(test.lis([69, 54, 19, 51, 16, 54, 64, 89, 72, 40, 31, 43, 1, 11, 82, 65, 75, 67, 25, 98, 31, 77, 55, 88, 85, 76, 35, 101, 44, 74, 29, 94, 72, 39, 20, 24, 23, 66, 16, 95, 5, 17,
                54, 89, 93, 10, 7, 88, 68, 10, 11, 22, 25, 50, 18, 59, 79, 87, 7, 49, 26, 96, 27, 19, 67, 35, 50, 10, 6, 48, 38, 28, 66, 94, 60, 27, 76, 4, 43, 66, 14, 8, 78, 72, 21, 56, 34, 90, 89]))
