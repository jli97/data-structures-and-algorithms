import heapq
from collections import defaultdict

# n - number of nodes in graph
# s - starting node
def dijkstra(adj, s):
    pq = [(s, 0)]
    dist = {}
    
    while pq:
        node, d = heapq.heappop(pq)
        if node in dist: 
            continue
        dist[node] = d
        for neighbour, d2 in adj[node]:
            if neighbour not in dist:
                heapq.heappush(pq, (neighbour, d + d2))
    
    return dist
