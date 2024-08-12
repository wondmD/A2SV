# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        leng = 0
        
        if head:
            temp = head
            while temp:
                temp = temp.next
                leng += 1
            pos = leng - (k % leng)
            temp = head
            print (leng, pos)
            if k%leng == 0 and head:
                return head
            while temp:
                if pos == 1:
                    temp2 = temp.next
                    temp.next = None
                    break
                temp = temp.next
                pos -= 1
            my_head = temp2
            while temp2:
                if temp2.next:
                    temp2 = temp2.next
                else:
                    temp2.next = head
                    break
            return (my_head)
        return None

