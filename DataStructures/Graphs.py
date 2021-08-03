import collections

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: Node) -> Node:
        if not node:
            return 
        
        copyNode = Node(node.val, [])
        queue = collections.deque([node]) # Can be done DFS as well
        m = {node: copyNode} #This maps the real nodes to the copy nodes
        
        while queue:
            node = queue.popleft()
            
            for neighbor in node.neighbors: 
                if neighbor not in m:    
                    neighborCopy = Node(neighbor.val, [])   #Create a copy
                    m[neighbor] = neighborCopy              #Map real node to copy
                    m[node].neighbors.append(neighborCopy)  #Append neighbor copy to node copy node's list of neighbors
                    queue.append(neighbor)                  #Queue neighbor
                else:
                    m[node].neighbors.append(m[neighbor])   #If we've traversed before, then append copy of neighbour to copy of node
        
        return copyNode 


