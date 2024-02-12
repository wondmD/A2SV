# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            temp1 = list1
            temp2 = list2
            if temp1.val <= temp2.val:
                head = temp1
                temp1 = temp1.next
            else:
                head = temp2
                temp2 = temp2.next 
            temp = head
            if temp1 and temp2:
                
                while temp1 and temp2:
                    if temp1.val <= temp2.val:
                        temp.next = temp1
                        temp1 = temp1.next
                    else:
                        temp.next = temp2
                        temp2 = temp2.next
                    temp = temp.next
            while temp1:
                temp.next = temp1
                temp = temp.next
                temp1 = temp1.next
            while temp2:
                temp.next = temp2
                temp = temp.next
                temp2 = temp2.next
            return (head)
        elif list1:
            return list1
        elif list2 :
            return list2 
        return None

