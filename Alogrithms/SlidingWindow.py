''' NOTES '''
# The problem will involve a data structure that is ordered and iterable like an array or string
# You are looking for some subrange in that array/string, like longest, shortest or target value
# There is an apparent brute force solution, this will reduce it to O(n)



''' Longest Substring Without Repeating Character '''

def slidingWindowExample(s):

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
    print("Result of slidingWindowExample:  " + str(slidingWindowExample(s)))

if __name__ == "__main__":
    main()
