class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        corner00 = min(A-1, B-1)
        corner08 = min(A-1, 8-B)
        corner80 = min(8-A, B-1)
        corner88 = min(8-A, 8-B)
        return corner00 + corner08 + corner80 + corner88


test = Solution()
print(test.solve(4, 4))
