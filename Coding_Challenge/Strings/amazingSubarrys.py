class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        # vowel = set('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        vowel = set('aeiouAEIOU')
        result = 0
        for i in range(len(A)):
            if A[i] in vowel:
                result += len(A) - i
        return result % 10003


test = Solution()
print(test.solve('ABEC'))
print(test.solve("pGpEusuCSWEaPOJmamlFAnIBgAJGtcJaMPFTLfUfkQKXeymydQsdWCTyEFjFgbSmknAmKYFHopWceEyCSumTyAFwhrLqQXbWnXSn"))
