class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word):
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            
            cur = cur.children[c]
        
        cur.isWord = True
    def searchWord(self, word): 
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isWord       
        
''' Doesn't account for edge case ["a", "aa", "aaa"..."a*n"]'''

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        t = Trie()
        
        for word in words:
            t.addWord(word)
        
        def search(word, idx, node, count, ret):
            if idx == len(word):
                if node == t.root and count > 1 and word not in ret: # If node == t.root, the last char
                    ret.add(word)                                    # was the end of a word
                return
                
            char = word[idx]
            
            if char in node.children:
                node = node.children[char]
                if node.isWord: # Two options use or not use this as a word
                    use = search(word, idx + 1, t.root, count + 1, ret) # Increment count, and start at root again
                    notUse = search(word, idx + 1, node, count, ret) 
                else:
                    search(word, idx + 1, node, count, ret)
            else:
                return
            
            
            
            
        ret = set()   
        for word in words:
            if word:
                search(word, 0, t.root, 0, ret)
            
        return list(ret)