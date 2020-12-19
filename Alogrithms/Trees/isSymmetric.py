def isSymmetric(root) -> bool:
    if root == None:
            return True
        
    def recursive(left, right):
        if left == None or right == None:
            return left == right
        
        if(left.val != right.val): 
            return False
        
        return recursive(left.left, right.right) and recursive(left.right, right.left) # This deals with the symmetry
    
    return recursive(root.left , root.right) 