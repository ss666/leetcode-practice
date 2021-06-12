# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while(cur is not None and cur.next is not None):
            if cur.val == cur.next.val: # more than two continuous duplicates
                cur.next = cur.next.next
            else: cur = cur.next  
        return head