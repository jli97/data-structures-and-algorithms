from functools import reduce

def strStr(haystack, needle):

        
        if (not haystack and not needle) or not needle:
            return 0
        
        if not haystack or len(haystack)<len(needle):
            return -1
        
    #Rabin Karp Algorithm
        
        base = 26 # 26 letters in the alphabet. We need this for shifting values to the left before adding the new hash. 289 * 10 = 2890
        values = [i for i in range(1,27)]
        
        hHash = reduce(lambda h, c: h * base + values[ord(c) - ord('a')], haystack[:len(needle)], 0) # hash of current window hence [:len(needle)]
        nHash = reduce(lambda h, c: h * base + values[ord(c) - ord('a')], needle, 0) # hash of needle

        '''
            functools.reduce is basically the following in one line

            nHash = 0
            for c in needle:
                nHash = nHash * base // Shift to left
                nHash = nHash + values[ord(c) - ord('a')] //Add new value to hash
        '''
        
        if hHash == nHash:
                return 0
        
        #Rolling hash
        for i in range(len(needle), len(haystack)):
            
            hHash -= (base ** (len(needle) - 1)) * values[ord(haystack[i - len(needle)]) - ord('a')] # Removes first value in the window
            hHash *= base # Shifts values to the left
            hHash += values[ord(haystack[i]) - ord('a')] #Adds new value to the hash

            if hHash == nHash:
                return i - len(needle) + 1
        

        return -1