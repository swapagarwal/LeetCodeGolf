'''
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space? 
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        a=b=head
        while b and b.next:
            a=a.next
            b=b.next.next
            if a==b:return True
        return False
