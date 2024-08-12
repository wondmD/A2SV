# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        slow = fast =  head
        f = 0
        while fast and fast.next:
            f = 1
            slow = slow.next
            fast = fast.next.next
            if fast == slow :
                break

        if f == 0 :
            return None
            
        temp = head 
        while temp and slow:
            if temp == slow:
                return slow
            temp = temp.next
            slow = slow.next
        return None
        
