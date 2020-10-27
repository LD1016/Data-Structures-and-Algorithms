class Solution:
    def solve(self, A):
        reverse = A[::-1]
        for i in range(1, len(A)):
            if reverse[:i] + A == reverse + A[-i:]:
                return i
        return 0


test = Solution()
print(test.solve("AACECAAAA"))
print(test.solve('ABC'))
print(test.solve('BCCA'))
