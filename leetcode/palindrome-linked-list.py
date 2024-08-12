# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []
        
        temp = head
        c = 0
        while temp:
            l.append(temp.val)
            temp = temp.next
            c+=1
        left = 0
        right = c-1

        while left < right:
            if l[left] != l[right]:
                return (False)
            left += 1
            right -= 1
        return (True)
        

