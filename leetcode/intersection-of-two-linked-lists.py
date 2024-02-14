# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lena = 0
        lenb = 0
        temp1 = headA
        temp2 = headB
        c1 = 0
        c2 = 0
        while temp1 or temp2:
            if temp1:
                temp1 = temp1.next
                c1+=1
            if temp2:
                temp2 = temp2.next
                c2+=1
        dif = abs(c1-c2)
        temp1 = headA
        temp2 = headB
        if c1 > c2:
            for i in range(dif):
                if temp1:
                    temp1 = temp1.next
        else :
            for i in range(dif):
                if temp2:
                    temp2 = temp2.next
        while temp1 and temp2:
            if temp1 == temp2:
                return temp1
            temp1 = temp1.next
            temp2 = temp2.next
        return None
