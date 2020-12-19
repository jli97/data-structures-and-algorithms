def isBalanced(root) -> bool:
    # Bottom up recursion
    # Each node returns its max depth of its right and left subtrees
    def check(root):
        if root is None:
            return 0
        left  = check(root.left)
        right = check(root.right)
        # If left or right is -1, the tree is unbalanced, keep returning -1
        # Check the difference in depth between left and right
        if left == -1 or right == -1 or abs(left - right) > 1: 
            return -1
        return 1 + max(left, right) # The depth of a ndoe is equal to the max depth
                                    # of its children nodes plus one
        
    return check(root) != -1