"""
Given an array of size n, find the majority element. The majority element is the 
element that appears more than floor(n/2) times.
You may assume that the array is non-empty and the majority element always exist in 
the array.

Example :

Input : [2, 1, 2]
Return  : 2 which occurs 2 times which is greater than 3/2.
"""


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        # if len(A) == 1:
        #     return A[0]
        # hashMap = {}
        # for i in A:
        #     if i not in hashMap:
        #         hashMap[i] = 1
        #     else:
        #         if hashMap[i]+1 > len(A)//2:
        #             return i
        #         hashMap[i] += 1
        # return 0
        curr_majority = A[0]
        cnt = 1
        for x in A[1:]:
            if x != curr_majority:
                cnt -= 1
            else:
                cnt += 1

            if cnt == 0:
                curr_majority = x
                cnt = 1

        return curr_majority


test = Solution()
print(test.majorityElement([2, 1, 2]))
