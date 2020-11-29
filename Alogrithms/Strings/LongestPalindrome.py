def longestPalindrome(self, s: str) -> str:
        #Expand Around Center Solution
        def expandAroundCenter(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return right - left - 1 # Returns the length of the longest palindromic 
                                    # subtring given those indicies and expanding
        
        if not s:
            return ""
        
        start, end = 0, 0 # keeps track of the solution indicies
        
        for i in range(len(s)):
            len1 = expandAroundCenter(s, i, i)
            len2 = expandAroundCenter(s, i, i + 1)
            l = max(len1, len2)
            
            # Check if longest length at this index is greater than the current max.
            # i is the center index, we want to get the starting index but dividing 
            # the length by 2 and adding/subtracting to get the start and end
            if l > end - start:            
                start = i - (l - 1) // 2   
                end = i + l // 2           
        
        return s[start: end + 1]