from collections import defaultdict

''' Bridge Identification Problem '''
#   The idea is to group all strongly connected nodes together to form
#   groups. Then find the edges that connect these strongly connected groups
#   
#   All nodes strongly connected together will have the same rank. This means
#   any ndoe with the same rank will stay connected, even if one edge within the
#   group is broken. 


def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        def dfs(ret, graph, low, visited, rank, prev, cur):
            visited[cur] = True
            low[cur] = rank
            
            for neighbor in graph[cur]:
                if neighbor == prev: # Do not check the edge that brought us here
                    continue
                
                if not visited[neighbor]:
                    dfs(ret, graph, low, visited, rank + 1, cur, neighbor)
                # After the dfs we will either have found a cycle or not.
                # If we found a cycle, then neighbor is a node that we have visited 
                # earlier and will have a lower rank. We mark the current node's low
                # value with that of the neighbor we visited earlier
                low[cur] = min(low[cur], low[neighbor]) 
                
                # If this neighbor node is not part of a cycle its rank will be higher
                # than the current rank
                if low[neighbor] > rank:    
                    ret.append([cur, neighbor])
            
            
        
        graph = defaultdict(list)
        rank = 0  # How far a node is from the starting node of the dfs
        low = [0] * n   # The lowest ranked node that can reach this node
        visited = [False] * n
        
        #Build graph
        for connection in connections:
            graph[connection[0]].append(connection[1])
            graph[connection[1]].append(connection[0])
        
        ret = []
        dfs(ret, graph, low, visited, 0, -1, 0)
        return ret