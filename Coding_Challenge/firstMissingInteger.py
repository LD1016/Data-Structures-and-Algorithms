class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        A.sort()
        result = 1
        for i in A:
            if i == result:
                result += 1
        return result

test = Solution()
print(test.firstMissingPositive([-8, -7, -6]))
print(test.firstMissingPositive([3,4,-1,1]))
print(test.firstMissingPositive([2, 0, 1]))