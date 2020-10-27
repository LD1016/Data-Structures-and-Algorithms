"""
Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.

Notes:

Expected solution is linear in time and constant in space.
For example,

List 1-->2-->1 is a palindrome.
List 1-->2-->3 is not a palindrome.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        lenA = 0
        copyA = A
        while copyA is not None:
            lenA, copyA = lenA + 1, copyA.next

        B, C = A, A
        prev = None
        nextNode = None
        i = 0
        while B is not None:
            nextNode = B.next
            if i >= (lenA//2):
                B.next = prev
            prev = B
            B = nextNode
            i += 1

        i = 0
        while i <= (lenA//2) and C is not None:
            if prev.val != C.val:
                return 0
            prev = prev.next
            C = C.next
            i += 1
        return 1
