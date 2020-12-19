import queue as queue
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
''' BUILD FUNCTIONS '''
def buildTree(arr): # Doesn't sort the array, so not valid BST

    if not arr:
        return None

    mid = (len(arr)) // 2 
    
    root = TreeNode(arr[mid]) 
    
    root.left = buildTree(arr[:mid]) 
    root.right  = buildTree(arr[mid+1:]) 

    return root

def buildBST(arr):
    if not arr:
        return None

    sort = sorted(arr)

    def helper(arr):
        if not arr:
            return None

        mid = (len(arr)) // 2 # If you want a balanced array, use the mid item as root
       
        root = TreeNode(arr[mid]) 
        
        root.left = helper(arr[:mid]) #splits the array for elements to the left
        root.right  = helper(arr[mid+1:]) #splits the array for elements to the right

        return root

    return helper(sort)

def validateBST(root): #In-order traversal of a BST. Prev must always be smaller
    if root == None:
        return True

    stack = queue.LifoQueue()
    prev = None

    while(root != None or stack.qsize() > 0):
        while(root != None): #Traverses left
            stack.put(root)
            root = root.left
        
        root = stack.get() #Traverses root
        if(prev != None and prev.val >= root.val):
            return False
        prev = root
        
        root = root.right #Traverses right 

    return True

''' TRAVERSALS '''
def iterativeInOrder(node):
    print('--- In-Order Iterative ---')

    stack = []
    ret = []
    while stack or node:
        if node:
            stack.append(node) 
            node = node.left # Go left
        else:
            node = stack.pop() 
            ret.append(node.val) # Visit node
            node = node.right # Go right

    return ret

def inOrderRecursive(root):
    print('--- In-Order Recursively ---')

    ret = []

    def helper(root, ret):
        if root == None:
            return
        helper(root.left, ret) # Traverse left
        ret.append(root.val) # Do something 
        helper(root.right, ret) #Traverse right

    helper(root, ret)
    return ret

def preOrderRecursive(root):
    print('--- Pre-Order Recursively ---')

    ret = []

    def helper(root, ret):
        if root == None:
            return
        
        ret.append(root.val)
        helper(root.left, ret)
        helper(root.right, ret)

    helper(root, ret)
    return ret

def preOrderIterative(root): 
    print('--- Pre-Order Iterative ---') 
    if root is None: 
        return 
  
    stack = [root]
  
    ret = []
    while stack: 
          
        cur = stack.pop() 
        ret.append(cur.val)
          
        if cur.right is not None:    # Put right in first because LIFO, 
            stack.append(cur.right)  # you want left to come out first
        if cur.left is not None: 
            stack.append(cur.left) 

    return ret

def postOrderRecursive(root):
    print('--- Post-Order Recursively ---')

    ret = []

    def helper(root, ret):
        if root == None:
            return
        
        helper(root.left, ret)
        helper(root.right, ret)
        ret.append(root.val)

    helper(root, ret)
    return ret

def levelOrderIterative(root): 
    ret = []

    if root == None:
        return ret
    
    q = deque() #Creates a FIFO queue
    q.append(root)

    while(q.empty() == False):

        node = q.popleft()
        ret.append(node.val)

        if node.left != None:
            q.append(node.left)
        if node.right != None:
            q.append(node.right)
    
    return ret


def main():
    arr = [7,4,9,3,5,1,8,2,6]
    root = buildBST(arr)

    print(iterativeInOrder(root))
    

    

if __name__ == "__main__":
    main()
