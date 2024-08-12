# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return
        leng = 0
        temp = head
        while temp:
            leng += 1
            temp = temp.next
        d = leng- n
        if d == 0:
            head = head.next
        temp = head
        d -= 1
        while temp:
            if d == 0:
                if temp.next:
                    temp.next = temp.next.next
                else:
                    temp.next = None
                return head
            d -= 1
            temp =temp.next
        return head
       