"""
LEETCODE 102: https://leetcode.com/problems/binary-tree-level-order-traversal/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        res = []
        q.append(root)

        while q:
            level_size = len(q)
            current_lvl = []

            for _ in range(level_size):
                node = q.popleft()
                current_lvl.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            res.append(current_lvl)
        return res