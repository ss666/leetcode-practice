class Solution{
    public ListNode middleNode(ListNode head){
        ListNode slow=head, fast=head;
        while(fast.next != null){
            if (fast.next.next != null){
                fast = fast.next.next;
                slow = slow.next;
            }
            else{
                slow = slow.next;
                break;
            }
        }
            return slow;
    }
}
