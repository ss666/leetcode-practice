# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy 
        cur = head
        
        while cur is not None and cur.next is not None:
            if cur.val == cur.next.val: #遇见重复节点
                cur=cur.next
                pre.next = cur.next
                if cur.next is not None and cur.val != cur.next.val: #处理到重复节点中的最后一个
                    cur=cur.next
            else: 
                pre = cur
                cur = cur.next
                
        return dummy.next # 此时dummy的next已经不是最初的head，因为dummy已经被pre修改过next
           