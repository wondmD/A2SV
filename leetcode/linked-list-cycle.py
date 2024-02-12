# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head:
            l = []
            temp = head
            l.append(temp)
            while True:
                if temp:
                    temp = temp.next
                    if temp in l:
                        return True
                    else:
                        l.append(temp)
                else:
                    break
            return False
        return (False)
