''' NOTES '''
# The problem will involve a data structure that is ordered and iterable like an 
# array or string. You are looking for some subrange in that array/string, like 
# longest, shortest or target value. There is an apparent brute force solution, 
# this will reduce it to O(n)



''' Longest Substring Without Repeating Character '''

def longestSubstringWithoutRepeatingChar(s):

    max_len = 0
    i = 0
    j = 0

    hash_set = set()

    while j < len(s):
        if s[j] not in hash_set:
            hash_set.add(s[j])
            j = j + 1
            max_len = max(len(hash_set), max_len)
        
        else:
            hash_set.remove(s[i])
            i = i + 1

    return max_len


def main():
    s = 'abcabcbb'
    print("Result of longestSubstringWithoutRepeatingChar:  " + str(longestSubstringWithoutRepeatingChar(s)))

''' Minimum Window Substring '''
def minWindow(self, s: str, t: str) -> str:
        m = {} #Keeps track of the number of instances for each char in t
        
        #populate the map
        for c in t:
            if c in m:
                m[c] += 1
            else:
                m[c] = 1
        
        start, end = 0, 0
        uniqueChars = len(list(m.keys()))
        ret = ""
        min_len = float('inf')
        
        while end < len(s):
            end_char = s[end]
            
            if end_char in m:
                m[end_char] -= 1
                if m[end_char] == 0:
                    uniqueChars -= 1
            
            end = end + 1
            
            while uniqueChars == 0:
                if end - start < min_len:
                    min_len = end - start
                    ret = s[start: end] # not end + 1, because right before we enter this loop, end is incremented 
                
                start_char = s[start]
                
                if start_char in m:
                    m[start_char] += 1
                    if m[start_char] > 0:
                        uniqueChars += 1
                
                start += 1
                
        
        return ret
if __name__ == "__main__":
    main()
