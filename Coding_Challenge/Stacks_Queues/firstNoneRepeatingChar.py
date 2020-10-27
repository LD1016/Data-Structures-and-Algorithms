class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        s = set()
        stack = []
        ans = []

        for i in A:
            if i not in s:
                s.add(i)
                stack.append(i)
                ans.append(stack[0])
            else:
                if i in stack:
                    stack.remove(i)
                if stack:
                    ans.append(stack[0])
                else:
                    ans.append('#')

        return "".join(ans)


test = Solution()
# print(test.solve("abadbc"))
# print(test.solve("abcabc"))
# print(test.solve("xxikrwmjvsvckfrqxnibkcasompsuyuogauacjrr"))
# print(test.solve("jyhrcwuengcbnuchctluxjgtxqtfvrebveewgasluuwooupcyxwgl"))
print(test.solve("hspkzrqozquywqsnumncuclkrrwsormkfprzotxrcotbnteiizlvt"))
