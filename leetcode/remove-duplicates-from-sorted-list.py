# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            temp = head
            while temp and temp.next:
                if temp.val == temp.next.val:
                    if temp and temp.next:
                        temp.next = temp.next.next
                    elif temp:
                        temp.next=None
                else:
                    temp = temp.next
            return (head)
        else:
            return None
        