# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # base case
        if head is None or head.next is None:  
            return head
        
        # recursive step
        # decompose a larger instance of the problem into one or more simpler or smaller instances that can be solved by recursive calls, 
        #and then recombines the results of those subproblems to produce the solution to the original problem.
        left = head
        mid = head.next
        right = mid.next
        mid.next = left 
        left.next = self.swapPairs(right)
        return mid

