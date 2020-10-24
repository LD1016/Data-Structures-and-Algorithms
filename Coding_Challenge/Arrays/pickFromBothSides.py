class Solution:
    def solve(self, A, B):
        partA = A[:B]
        maxVal = sum(partA)
        for i in range(len(A)-B):
            lastA = A.pop()
            partA.pop()
            partA.insert(0, lastA)
            maxVal = max(maxVal, sum(partA))
        return maxVal


test = Solution()
print(test.solve([5, -2, 3, 1, 2], 3))
