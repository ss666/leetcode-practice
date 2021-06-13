# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#iteration 
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur is not None: 
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

#recursion
 class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        reversed_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return reversed_head # return the head of the reversed list