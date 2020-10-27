# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        lenA = self.getLength(A)
        lenB = self.getLength(B)
        if lenA > lenB:
            return self.helper(A, lenA, B, lenB)
        return self.helper(B, lenB, A, lenA)

    def helper(self, A, lenA, B, lenB):
        diff = lenA - lenB
        while diff > 0:
            diff, A = diff - 1, A.next
        while A != None and B != None:
            if A == B:
                return A
            A, B = A.next, B.next
        return None

    def getLength(self, A):
        result = 0
        while A != None:
            result, A = result + 1, A.next
        return result


"""

Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3

"""
