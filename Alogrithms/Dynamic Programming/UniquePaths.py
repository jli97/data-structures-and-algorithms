''' Explanation of Recursion -> DP '''

''' Recursion '''

def uniquePaths(self, m: int, n: int) -> int:
        
    def helper(x, y):
        if x > m - 1 or y > n - 1:    # Base case, outside of range
            return 0
        if x == m - 1 and y == n - 1: # Reached target
            return 1
        
        right = helper(x, y + 1) # Return all possible paths from the right
        up = helper(x + 1, y)    # Return all possible paths from the top
        
        return right + up #Return the sum
    
    return helper(0,0)
    
''' Top Down DP / Memoization '''
def uniquePaths(self, m: int, n: int) -> int:
        #Notice the similarities to the recursive solution
        def helper(x, y, cache):
            if x > n - 1 or y > m - 1:
                return cache[x][y]      # cache[x][y] is already 0, so simply return it
            if x == n - 1 and y == m - 1:
                cache[x][y] = 1         # Same as returning 1, but we want to cache
                return cache[x][y]      # the result
            
            if cache[x][y] == -1:        # If we haven't cached anything at this index
                right = helper(x, y + 1, cache)
                up = helper(x + 1, y, cache)
                cache[x][y] = right + up # Cache the result
            
            return cache[x][y] 
            
        
        cache = [[-1] * (m + 1) for _ in range(n + 1)]
        return helper(0,0, cache) 

''' Bottom up DP / Tabulation ''' 
def uniquePaths(self, m: int, n: int) -> int:
        
    def helper(x, y):
        if x == m and y == n:
            return 1
        
        right = helper(x, y + 1)
        up = helper(x + 1, y)
        
        return right + up
    
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1 # Number of paths to the starting is 1

    for i in range(m):
        for j in range(n):
            if i == 0:          # Can only go up or to the right, so there is only 
                dp[i][j] = 1    # one way to reach the bottom or the left side
            elif j == 0:        # of the matrix
                dp[i][j] = 1
            else:
                # Number of paths to a cell is equal to the number of paths to
                # the left cell and bottom cell 
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] 

    return dp[-1][-1] 