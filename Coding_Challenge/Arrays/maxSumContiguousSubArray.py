"""
Find the contiguous subarray within an array, 
A of length N which has the largest sum.

Input 1:
    A = [1, 2, 3, 4, -10]
Output 1:
    10
Explanation 1:
    The subarray [1, 2, 3, 4] has the maximum possible sum of 10.

Input 2:
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output 2:
    6
Explanation 2:
    The subarray [4,-1,2,1] has the maximum possible sum of 6.
"""


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        if len(A) < 1:
            return 0
        ans = -float("inf")
        temp = 0
        for i in range(len(A)):
            if A[i] > temp + A[i]:
                temp = A[i]
            else:
                temp = temp + A[i]
            ans = max(temp, ans)
        return ans


test = Solution()
print(test.maxSubArray([1, 2, 3, 4, -10]))
print(test.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
