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
        
    def searchWord(self, word): 
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isWord #If you make it to the last c in word, check if the word is valid
     
    def searchPrefix(self, prefix): #Searches for if prefix exists, does not check if word
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True