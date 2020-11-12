"""
Problem Description:
Given a Linked List A consisting of N nodes.
The Linked List is binary i.e data values in the linked list nodes consist 
of only 0's and 1's. You need to sort the linked list and return the new linked list.

NOTE:
Try to do it in constant space.
Problem Constraints
1 <= N <= 105
A.val = 0 or A.val = 1

Example Input
Input 1:
 1 -> 0 -> 0 -> 1
Input 2:
 0 -> 0 -> 1 -> 1 -> 0

Example Output
Output 1:
 0 -> 0 -> 1 -> 1
Output 2:
 0 -> 0 -> 0 -> 1 -> 1
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        zeros, n = 0, 0
        B, C = A, A
        while B is not None:
            if B.val == 0:
                zeros += 1
            B, n = B.next, n+1
        while n > 0:
            if zeros != 0:
                C.val = 0
                zeros -= 1
            else:
                C.val = 1
            C, n = C.next, n-1
        return A
