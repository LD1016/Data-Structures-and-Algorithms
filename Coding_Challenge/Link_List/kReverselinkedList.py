"""
Given a singly linked list and an integer K, reverses the nodes of the

list K at a time and returns modified linked list.

 NOTE : The length of the list is divisible by K 
Example :

Given linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 and K=2,

You should return 2 -> 1 -> 4 -> 3 -> 6 -> 5

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):
        if B <= 1:
            return A
        nodes = []
        vals = []
        count = 0
        copy = A
        while copy is not None:
            if count < B:
                nodes.append(copy)
                vals.append(copy.val)
                count += 1
                copy = copy.next
            else:
                count = 0
                for i in range(B):
                    node = nodes.pop(0)
                    node.val = vals.pop()
        for i in range(B):
            node = nodes.pop(0)
            node.val = vals.pop()
        return A
