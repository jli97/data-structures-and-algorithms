def maxPathSum(self, root: TreeNode) -> int:
        def pathSum(node):
            nonlocal maxSum
            if not node:
                return 0
            
            l = max(0, pathSum(node.left)) # Max between 0, because you can choose to not use a node
            r = max(0, pathSum(node.right))

            #Check if this node as root is greatest path
            maxSum = max(maxSum, l + r + node.val) 
            
            return node.val + max(l, r) # Return the maxSum from this node assuming 
                                        # this node is not the root of the max path
            
        maxSum = float('-inf')
        pathSum(root)
        return maxSum