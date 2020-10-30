'''NOTES'''
# The algorithm starts off by building the basic well-formed combination '((()))'
# it then returns to the iteration where n_open == n - 1 and instead of placing
# an opening as it is currently evaluating if n_open < n_close 

def generateParenthesis(self, n):
        def backtrack(n_open, n_close, cur, ret): #n_open n_close keeps track of number of open/closed parentheses available to be used
            #Choose between adding an open or close 
            if n_open > 0:
                backtrack(n_open - 1, n_close, cur + '(', ret)
                
            if n_open < n_close:
                backtrack(n_open, n_close - 1, cur + ')', ret)
            
            if n_close == 0:
                ret.append(cur)
            
            return
            
            
        
        ret = []
        backtrack(n, n, '', ret)
        return ret