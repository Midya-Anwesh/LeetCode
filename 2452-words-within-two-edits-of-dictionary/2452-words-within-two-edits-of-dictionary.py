class TrieNode:
    def __init__(self):
        self.childs = [None for _ in range(26)]
        self.wordEnd = False

class Trie:
    def __init__(self):
        self.root = None
    
    def insert(self, word: str) -> None:
        if self.root is None:
            self.root = TrieNode()
        node = self.root
        idx = 0
        while idx < len(word):
            curr = ord(word[idx]) - 97
            if node.childs[curr] is None:
                node.childs[curr] = TrieNode()
            node = node.childs[curr]
            idx += 1
            if idx >= len(word):
                node.wordEnd = True
    
    def find(self, editsAllowed: int, word: str) -> bool:
        if self.root is None:
            return False
        node = self.root

        def dfs(node: Optional[TrieNode], edits: int, idx: int) -> bool:
            curr = ord(word[idx]) - 97
            found = False
            # If it's the last letter
            if idx == len(word)-1:
                # If we have edits available just return true if ther is any word available of the same length
                if edits > 0:
                    for i in range(26):
                        if node.childs[i] is not None:
                            found |= node.childs[i].wordEnd
                # Othwise return if it's a word end
                if node.childs[curr] is not None:
                    found |= node.childs[curr].wordEnd
                return found

            # Traverse for current letter in trie
            if node.childs[curr] is not None:
                found |= dfs(node.childs[curr], edits, idx+1)

            # If not found try with edits
            if (not found) and (edits > 0):
                for i in range(26):
                    if node.childs[i] is None:
                        continue
                    found |= dfs(node.childs[i], edits-1, idx+1)
            
            # Return the result
            return found
        
        return dfs(node, editsAllowed, 0)


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        ret = []
        for word in queries:
            if trie.find(2, word):
                ret.append(word)
        return ret