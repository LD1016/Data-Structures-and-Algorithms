def reverseList(A):
    prev = None
    cur = A
    while cur != None:
        fut = cur.next
        cur.next = prev
        prev = cur
        cur = fut
    return prev


"""
Reverse a linked list. Do it in-place and in one-pass.

For example:
Given     1->2->3->4->5->NULL
return    5->4->3->2->1->NULL
"""
