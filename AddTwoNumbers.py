# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def helper(l1,l2,cb): 
            if l1 is None and l2 is None and cb==0:
                return None
            
            if l1 is None:
                l1 = ListNode(0)
            if l2 is None:
                l2 = ListNode(0)
                
            l1.val, cb = (l1.val+l2.val+cb) % 10, (l1.val+l2.val+cb) // 10
            l1.next = helper(l1.next,l2.next,cb)
            
            return l1
        
        
        l1 = helper(l1,l2,0)
        return l1