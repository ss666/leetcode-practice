# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
                
        def middleNode(head):
            slow, fast = head, head
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def reverseList(head):
            if head is None or head.next is None:
                return head
            
            reversed_head = reverseList(head.next)
            head.next.next = head#.next
            head.next = None

            return reversed_head
            
            
        mid = middleNode(head)
        mid_next = mid.next
        mid.next = None # 断开链表
        
        l1 = head
        l2 = reverseList(mid_next)
        
        while l2 is not None: #or l2.next is not None:
            l1_nxt = l1.next
            l1.next = l2
            l2_nxt = l2.next
            l2.next = l1_nxt
            
            l1 = l1_nxt
            l2 = l2_nxt

        
