def partitionLabels(self, S):
        m = {}
        ret = []
        
        for i, c in enumerate(S): #Get the index of the last occurance of each character and save it in a map
            if c not in m:
                end = len(S) - 1
                while end > i:
                    if S[end] == c:
                        break
                    end -= 1
                
                m[c] = end
        
        start = 0
        end = 0     #end represents the furthest last index of all the characters within S[start:end]
        
        for i, c in enumerate(S): 
            end = max(end, m[c]) #Update the farthest last index of all characters within S[start:end]
            if end == i: #Then we know this paritition includes all occurances of all the chracters
                ret.append(end - start + 1)
                start = end + 1
        
        return ret