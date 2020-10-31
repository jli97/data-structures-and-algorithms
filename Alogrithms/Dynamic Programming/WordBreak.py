''' TOP DOWN / MEMOIZATION '''
def wordBreakTD(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        def helper(s, wordDict, cache, start, end):
        
            while end < len(s):
                if s[start:end + 1] in wordDict:
                    if end == len(s) - 1:
                        return True

                    if (start, end) not in cache:
                        #Chose to use word
                        newStart = end + 1
                        newEnd = newStart
                        use = helper(s, wordDict, cache, newStart, newEnd)

                        #Chose not to use word
                        ignore = helper(s, wordDict, cache, start, end + 1)
                    
                    
                        #Save result
                        if use == False and ignore == False:
                            cache.add((start, end))

                        else:
                            return True # One was true
                    else:
                        return False

                end += 1
            
            return False
                
        cache = set() #keep track of if a pair of indexes lead to false
        return helper(s, wordDict, cache, 0, 0)


''' BOTTOM UP '''
def wordBreakBU(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [None] * (len(s) + 1)
        dp[0] = True #Base case, any word in the dict with starting index at 0 is part of the solution
        
        for i in range(1, len(s) + 1): #At each index i, check every substring from (0 -> i, i)
            for j in range(i):
                substr = s[j : i]
                if substr in wordDict and dp[j]: #dp[j] is whether or not a valid word ended at this index - 1
                    dp[i] = True # This marks the next index where a potential substring can start 
                    break
        
        return dp[len(s)]