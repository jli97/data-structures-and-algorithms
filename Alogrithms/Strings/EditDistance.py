def minDistance(self, word1: str, word2: str) -> int:
    
    def helper(idx_1: int, idx_2: int):
        if idx_1 < 0: # end of word1, insert/delete rest of word2
            return idx_2 + 1
        
        if idx_2 < 0: # end of word2, insert/delete rest of word1
            return idx_1 + 1
        
        if distance_matrix[idx_1][idx_2] == -1: # Have yet to traverse this differnece between word1[0:idx_1] and word2[0:idx_2]
            if word1[idx_1] == word2[idx_2]: # If the characters are equal, then continue with idx_1 - 1 and idx_2 - 1
                distance_matrix[idx_1][idx_2] = helper(idx_1 - 1, idx_2 - 1)
                
            else:
                substitute_last = helper(idx_1 - 1, idx_2 - 1)
                add_last = helper(idx_1 - 1, idx_2)
                delete_last = helper(idx_1, idx_2 - 1)
                
                distance_matrix[idx_1][idx_2] = 1 + min(substitute_last, add_last, delete_last)
        
        return distance_matrix[idx_1][idx_2]
        
    
    distance_matrix = [[-1] * len(word2) for _ in word1]
    return helper(len(word1) - 1, len(word2) - 1)