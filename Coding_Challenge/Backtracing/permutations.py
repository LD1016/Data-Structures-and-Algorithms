"""
Given a collection of numbers, return all possible permutations.

Example:

[1,2,3] will have the following permutations:

[1,2,3]
[1,3,2]
[2,1,3] 
[2,3,1] 
[3,1,2] 
[3,2,1]
"""


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        if len(A) == 1:
            return [A]
        result = []
        for i in range(len(A)):
            sub = self.permute(A[:i]+A[i+1:])
            for j in sub:
                result.append([A[i]] + j)
        return result


test = Solution()
print(test.permute([1, 2, 3]))
print()
print(test.permute([1, 2, 3, 4]))
