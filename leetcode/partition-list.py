# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head: 
            return None
        v1 = less = None
        dummy_head = not_less = None
        temp = head
        while temp:
            if temp.val <x:
                if not less:
                    less= temp
                    v1 = temp
                else:
                    less.next = temp
                    less = temp
            else:
                if not not_less:
                    not_less= temp
                    dummy_head = temp
                else:
                    not_less.next = temp
                    not_less = temp
            temp = temp.next
            
        if less and dummy_head:
            less.next = dummy_head
        if not_less:
            not_less.next = None
        if v1:
            return v1
        else:
            return dummy_head