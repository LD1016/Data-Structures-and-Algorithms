"""
Given an unsorted integer array, find the first missing positive integer.

Example:

Given [1,2,0] return 3,

[3,4,-1,1] return 2,

[-8, -7, -6] returns 1

Your algorithm should run in O(n) time and use constant space.
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        # A.sort()
        # ans = 1
        # for i in A:
        #     if i == ans:
        #         ans += 1
        # return ans
        # setNums = set()
        # for i in A:
        #     setNums.add(i)
        # for i in range(1, len(A)+1):
        #     if i not in setNums:
        #         return i
        # return len(A)+1

        n = len(A)
        if 1 not in A:
            return 1
        if n == 1:
            return n+1
        for i in range(n):
            if A[i] <= 0 or A[i] > n:
                A[i] = 1
        for i in range(n):
            a = abs(A[i])
            if a == n:
                A[0] = - abs(A[0])
            else:
                A[a] = - abs(A[a])
        for i in range(1, n):
            if A[i] > 0:
                return i
        if A[0] > 0:
            return n
        return n+1


test = Solution()
print(test.firstMissingPositive([1, 8, 9, 11, 12, -3, 0]))
print(test.firstMissingPositive([1, 2, 0]))
print(test.firstMissingPositive([-8, -7, -6]))
print(test.firstMissingPositive([3, 4, -1, 1]))
