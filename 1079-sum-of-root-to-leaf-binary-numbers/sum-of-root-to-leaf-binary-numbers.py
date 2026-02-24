class Solution:
    def sumRootToLeaf(self, root):
        def dfs(node, current):
            if not node:
                return 0
            
            # Update current value
            current = (current << 1) | node.val
            
            # If leaf node
            if not node.left and not node.right:
                return current
            
            # Recurse left and right
            return dfs(node.left, current) + dfs(node.right, current)
        
        return dfs(root, 0)