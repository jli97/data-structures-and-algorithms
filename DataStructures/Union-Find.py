class UnionFind:
    def __init__(self, size):
        self.size = size
        self.numComponents = size
        self.sz = [0] * size # Tracks the size of each component
        self.parent = [0] * size # Tracks the parent of each node, id[i] -> parent of i

        for i in range(size):
            self.id[i] = i
            self.sz[i] = 1
        
    # Finds the root of p
    def find(self, p):
        # Find the root of the component/set
        root = p
        while root != self.parent[root]:
            root = self.parent[root]

        # Path compression
        while p != root:
            next = self.parent[p]
            self.parent[p] = root
            p = next
        
        return root
    
    # Connected nodes have the same root
    def connected(self, p, q):
        return self.find(p) == self.find(q)
    
    # Connects p and q
    def unify(self, p, q):
        if self.connected(p, q):
            return 

        root1 = self.find(p)
        root2 = self.find(q)

        # Merge smaller component into the larger one
        if self.sz[root1] < self.sz[root2]:
            self.sz[root2] += self.sz[root1]
            self.parent[root1] = root2
        else:
            self.sz[root1] += self.sz[root2]
            self.parent[root2] = root1
        
        self.numComponents -= 1

    def componentSize(self, p):
        return self.sz[self.find(p)]
    
    def size(self):
        return self.size
    
    def components(self):
        return self.numComponents
    
