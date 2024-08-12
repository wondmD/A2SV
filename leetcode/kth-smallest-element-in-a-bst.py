# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def inord(node):
            if node:
                inord(node.left)
                if node.val or node.val ==0:
                    res.append(node.val)
                inord(node.right)
        inord(root)
        c =1
        return (res[k-1])
