# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def find(node, v1, v2):
            if node:
                print(node.val, v1, v2)
                if node.val == v1 or node.val == v2:
                    return node
                elif node.val > v1 and node.val > v2:
                    return find(node.left, v1, v2)
                elif  node.val < v1 and node.val < v2:
                    return find(node.right, v1, v2)
                else:
                    return node
                
        return find(root, p.val, q.val)
