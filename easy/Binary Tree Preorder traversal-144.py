"""Preorder Traversal
Order → Root → Left → Right
The rule is simple — visit the parent first, then go left, then go right.
        1
       / \
      2   3
     / \
    4   5

    Start at 1 → append 1 ✅

Go LEFT to 2 → append 2 ✅

Go LEFT to 4 → append 4 ✅
  4 has no children → go back up

Go RIGHT to 5 → append 5 ✅
  5 has no children → go back up

Go RIGHT to 3 → append 3 ✅
  3 has no children → done

Result → [1, 2, 4, 5, 3]
"""
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node):
            if node is None:
                return
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return result

# Build the tree
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node1.left  = node2
node1.right = node3
node2.left  = node4
node2.right = node5

# Run and print
sol = Solution()
print(sol.preorderTraversal(node1))