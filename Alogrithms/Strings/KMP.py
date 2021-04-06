def KMP(s1, s2):
    def prefixFunction(s):
        p = [0] * len(s)
        j = 0

        for i in range(1, len(s)):
            while j > 0 and s[j] != s[i]:
                j = p[j - 1]
            
            if s[j] == s[i]:
                j += 1
            p[i] = j

        return p

    if len(s2) > len(s1):
        return False

    prefix_table = prefixFunction(s2)
    i, j = 0, -1
    
    while i < len(s1):
        if s1[i] == s2[j + 1]:
            j += 1
            if j == len(s2) - 1:
                return True
        else:
            while s1[i] != s2[j + 1] and j > -1:
                if prefix_table[j] - 1 == 0:
                    j = -1
                j = prefix_table[j] - 1
            if s1[i] == s2[j + 1]:
                j += 1
        i += 1

    return False


