# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode.com/problems/construct-string-from-binary-tree/description/
class Solution:
    def tree2str(self, root: TreeNode) -> str:
        if not root:
            return ""
        
        stack = [root]
        visited = set()
        res = ""
        
        while stack:
            node = stack[-1]
            if node in visited:
                stack.pop()
                res += ")"
            else:
                visited.add(node)
                res += "(" + str(node.val)
                if not node.left and node.right:
                    res += "()"
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        
        return res[1:-1]
       
