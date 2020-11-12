"""
Problem Description:
Given a linked list A of length N and an integer B.
You need to find the value of the Bth node from the middle towards 
the beginning of the Linked List A.
If no such element exists, then return -1.

NOTE:
Position of middle node is: (N/2)+1, where N is the total number of nodes in the list.

Example Input
Input 1:
 A = 3 -> 4 -> 7 -> 5 -> 6 -> 1 6 -> 15 -> 61 -> 16
 B = 3
Input 2:
 A = 1 -> 14 -> 6 -> 16 -> 4 -> 10
 B = 2
Input 3:
 A = 1 -> 14 -> 6 -> 16 -> 4 -> 10
 B = 10
 
Example Output
Output 1:
 4
Output 2:
 14
Output 3:
 -1
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        # n = 0
        # C = A
        # while C is not None:
        #     n, C = n + 1, C.next
        # middle = (n//2) + 1
        # middleNode = A
        # while middle > 1:
        #     middle, middleNode = middle - 1, middleNode.next
        # prev = None
        # cur = A
        # while cur is not None:
        #     fut = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = fut
        # while middleNode is not None and B > 0:
        #     B -= 1
        #     middleNode = middleNode.next
        # if middleNode is None:
        #     return -1
        # else:
        #     return middleNode.val
        lenL = 0
        head = thead = A

        # Calculate length of linked list
        while head is not None:
            head = head.next
            lenL += 1

        mid = (lenL//2) + 1

        # Find kth node
        if B < mid:
            j = 0
            while thead is not None:
                if j == mid - B - 1:
                    return thead.val
                thead = thead.next
                j += 1
        else:
            return -1
