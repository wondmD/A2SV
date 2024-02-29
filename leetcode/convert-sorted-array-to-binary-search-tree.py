# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def majic(left, right):
            if left > right:
                return
            if left == right:
                return TreeNode(nums[left])
            
            mid = math.ceil((right+left)/2)
            root = TreeNode(nums[mid])
            root.left = majic(left, mid-1)
            root.right = majic(mid+1, right)
            return root
        return majic(0, len(nums)-1)            