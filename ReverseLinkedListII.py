# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        m,n=left,right
        if head is None or head.next is None or m==n:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        start = dummy
        for i in range(0,m-1):
            start = start.next
            
        pre, cur = None, start.next #=None，断掉m的next
        end = cur #保留m
        for i in range(0,n-m+1):
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        
        start.next = pre
        end.next = cur #重连m的next
        return dummy.next

        