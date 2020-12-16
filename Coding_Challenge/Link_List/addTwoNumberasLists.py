"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

    342 + 465 = 807
Make sure there are no trailing zeros in the output list
So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        remain = 0
        result = ListNode(1)
        cur = result
        while A is not None and B is not None:
            temp = A.val + B.val if remain == 0 else A.val + B.val + 1
            if temp >= 10:
                remain = 1
            node = ListNode(temp % 10)
            cur.next = node
            cur = cur.next
        if A is not None:
            self.helper(A, cur, remain)
        elif B is not None:
            self.helper(B, cur, remain)
        elif remain == 1:
            node = ListNode(1)
            cur.next = node
        return result.next

    def helper(self, A, B, R):
        node = None
        while A is not None:
            if R == 1:
                node = ListNode(A.val + R)
                R = 0
            else:
                node = ListNode(A.val)
            B.next = node
            B = B.next
            A = A.next
