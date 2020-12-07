from collections import defaultdict
def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return range(numCourses)
        
        def dfs(root, status, forward):
            nonlocal isPossible
            nonlocal topological_order
            
            if isPossible == False:
                return
            if root is None:
                return
            if status[root] == 1:
                isPossible = False
                return   
            if status[root] == 2:
                return
            
            status[root] = 1
            
            for course in forward[root]:
                dfs(course, status, forward)
            
            # Nodes at the end of the dfs, get appended first. Nodes at the end 
            # of a dfs are not pre-reqs, and such should go first
            topological_order.append(root) 
            status[root] = 2            
        
        forward = defaultdict(set)
        status = [0] * numCourses
        isPossible = True
        
        for pair in prerequisites:
            forward[pair[1]].add(pair[0])
        
        topological_order = [] 
        
        for i in range(numCourses):
            if status[i] == 0:
                r = dfs(i, status, forward)

        return reversed(topological_order) if isPossible else []

