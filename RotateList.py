# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head
        
        len_ = 1
        fast = head
        while fast.next is not None:
            fast = fast.next 
            len_ +=1
            
        loc = k % len_
        
        dist = len_ - loc
        
        slow=head
        for i in range(dist-1):
            slow= slow.next

        fast.next = head
        new_head = slow.next
        slow.next = None
        
        return new_head
            