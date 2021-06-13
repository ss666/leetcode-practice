# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        def reverseList(cur):
            if cur is None or cur.next is None:
                return cur
            
            reversed_head = reverseList(cur.next)
            cur.next.next = cur
            cur.next = None
            
            return reversed_head
        
        def middleNode(head):
            dummy = ListNode(-1)
            dummy.next = head
        
            slow, fast = dummy, dummy
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
            return slow
    
    
    
        mid = middleNode(head)
        mid_next = mid.next
        head2 =  reverseList(mid_next)
               
        while head2 is not None:
            if head.val == head2.val:      
                head = head.next 
                head2 =head2.next
            else:
                return False
        return True

