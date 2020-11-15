from collections import defaultdict

def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
    def dfs(node, visited):
        stack = [node]
        
        while stack:
            cur = stack.pop()
            visited.add(cur)
            
            for neighbor in g[cur]:
                if neighbor not in visited:
                    stack.append(neighbor)
    
    
    
    g = defaultdict(set)
    visited = set()
    count = 0
    
    # Construct undirected graph
    for edge in edges:
        g[edge[0]].add(edge[1])
        g[edge[1]].add(edge[0])
    
    # DFS through all nodes. Each call to DFS is a new connected
    # component because any visited node is part of another connected
    # component in which previous dfs calls have marked as visited
    for i in range(n):
        if i not in visited:
            dfs(i, visited)
            count += 1
    
    return count