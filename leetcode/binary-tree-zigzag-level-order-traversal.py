# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dt = defaultdict(list)
        def zigzag(node,level):
            if node:
                dt[level].append(node.val)
                zigzag(node.left,level+1)
                zigzag(node.right,level+1)
                
        zigzag(root,0)
        ans = []
       
        for i in dt:
            if i%2==0:
                ans.append(dt[i])
            else:
                ans.append(dt[i][::-1])
        return ans