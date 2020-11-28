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
        A.sort()
        ans = 1
        for i in A:
            if i == ans:
                ans += 1
        return ans


test = Solution()
print(test.firstMissingPositive([-8, -7, -6]))
print(test.firstMissingPositive([3, 4, -1, 1]))
print(test.firstMissingPositive([2, 0, 1]))
