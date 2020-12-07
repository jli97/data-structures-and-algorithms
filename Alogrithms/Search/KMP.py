def strStr(self, haystack: str, needle: str) -> int:
        if not haystack and not needle:
            return 0
        elif not haystack:
            return -1
        elif not needle:
            return 0
        
        if len(haystack) < len(needle):
            return -1
        
        #KMP Pattern Matching
        
        # At each i, table[i] = the longest prefix that is also a
        # suffix up to needle[:i+1] 
        table = [0] * len(needle)
        
        #Populate the table
        start, end = 0, 1
        
        while end < len(needle):
            if needle[start] == needle[end]:
                start += 1
                table[end] = start
                end += 1
            else:
                if start != 0:
                    start = table[start - 1] 
                else:
                    end += 1

        #Search using table
        j = 0 # Needle idx
        
        for i in range(len(haystack)):
            if haystack[i] == needle[j]:
                j += 1
                if j == len(needle):
                    return i - len(needle) + 1
            else:
                while j != 0:
                    j = table[j - 1] #
                    if needle[j] == haystack[i]:
                        j += 1
                        break
        return -1
        