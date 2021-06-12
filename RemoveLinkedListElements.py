# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        while(cur is not None and cur.next is not None):
            if cur.next.val == val:
                cur.next = cur.next.next
            else: cur = cur.next
        return dummy.next

    #using dummy node
        