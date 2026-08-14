# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sameTree(self, root1, root2):
        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False
        elif root1.val != root2.val:
            return False
        
        left = self.sameTree(root1.left, root2.left)
        right = self.sameTree(root1.right, root2.right)

        return left and right
            
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return self.sameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

        