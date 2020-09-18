class Solution(object):
    def solveNQueens(self, n):
        
        def solveRow(row):
            if row == n:
                #All queens are placed
                result.append(list(col_placement[:row]))
                return
            
            for col in range(n):
                # Check if col is valid 
                
                if all(abs(c - col) not in (0, row - i) for i, c in enumerate(col_placement[:row])): # abs(c - col) not in (0, row - i) checks for both diagonal (row - i) and column (0)
                    col_placement[row] = col    
                    solveRow(row + 1)           # If this for-loop ends without making it here, we will go back to the last recursive call and try other cols
                
        result, col_placement = [], [0] * n
        solveRow(0)
        
        return result