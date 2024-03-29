# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        q = deque([root])

        while q:
            level_vals = []
            level_size = len(q)

            for _ in range(level_size):
                node = q.popleft()
                level_vals.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans.append(level_vals)

        return ans
      
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
