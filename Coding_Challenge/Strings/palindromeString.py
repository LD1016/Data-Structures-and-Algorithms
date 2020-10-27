class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        temp = []
        for i in A:
            if i.isalpha() or i.isnumeric():
                temp.append(i.lower())
        reversTemp = list(reversed(temp))
        print(temp, reversTemp)
        return 1 if temp == reversTemp else 0


test = Solution()
print(test.isPalindrome("A man, a plan, a canal: Panama"))
print(test.isPalindrome("1a2"))
