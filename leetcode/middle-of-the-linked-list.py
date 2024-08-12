# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            temp = head
            c = 0
            while True:
                if temp:
                    temp = temp.next
                    c+=1
                else:
                    break
            idx = c//2
            temp = head
            for i in range(idx):
                temp  = temp.next
            return (temp)
        else:
            return (0)

                
        