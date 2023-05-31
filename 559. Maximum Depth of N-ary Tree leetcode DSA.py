"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        queue = [root]
        depth = 0
        while queue:
            depth += 1
            level_size = len(queue)
            for i in range(level_size):
                node = queue.pop(0)
                for child in node.children:
                    queue.append(child)
        
        return depth
# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
