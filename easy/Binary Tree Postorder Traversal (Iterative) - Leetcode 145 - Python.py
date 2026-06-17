"""Given the root of a binary tree, return the postorder traversal of its nodes' values.
Example 1:

Input: root = [1,null,2,3]

Output: [3,2,1]

Explanation:

The postorder traversal is: left -> right -> root.
"""
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)

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
print(sol.postorderTraversal(node1))