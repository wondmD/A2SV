# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and q:
            return False
        elif not q and p:
            return False
        elif not p and not q:
            return True
        else:
            if  p.val != q.val:
                return False
            x = self.isSameTree(p.left, q.left)
            if not x:
                return x
            y = self.isSameTree(p.right, q.right)
            if not y:
                return y
        return True
            
