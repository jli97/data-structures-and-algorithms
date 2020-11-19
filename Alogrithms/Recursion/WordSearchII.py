class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word):
        cur = self.root #Start at root
        for c in word: 
            if c not in cur.children: #If c is not in children, create a new node and attach it
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True # Mark the last node as a word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #Create a Trie and add words to it
        t = Trie() 
        
        for word in words:
            t.addWord(word)
        
        def dfs(i, j, visited, node, curWord, ret):
            if visited[i][j]:
                return

            char = board[i][j]
            
            if node.isWord and curWord not in ret: # Check if we have an asnwer
                ret.append(curWord)                # Don't return immediately as you may
                                                   # have words that are prefixes of others
                                                   # Ex. abc, abcde, abcdef

            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for d in directions:
                r = i + d[0]
                c = j + d[1]
                
                if (r >= 0 and r < len(board) and c >= 0 and c < len(board[0])): #Ensure correct bounds
                    nextChar = board[r][c]
                    if nextChar in node.children:
                        # Check for visited here and not at the beginning of the dfs
                        # because you only want to mark them as visited if they lead 
                        # to the next character. It is possible that the char that doesn't 
                        # lead to the next char, is needed later in the string and shouldn't be 
                        # already marked visited 
                        visited[i][j] = True    
                        dfs(r, c, visited, node.children[nextChar], curWord+nextChar, ret)

        ret = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                # Start dfs if you find a character equal to the first character of a word
                if board[i][j] in t.root.children: 
                    visited = [[False] * len(board[0]) for _ in range(len(board))]
                    dfs(i, j, visited, t.root.children[board[i][j]], ""+board[i][j], ret)

        return ret