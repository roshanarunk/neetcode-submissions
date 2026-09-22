class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for x in word:
            if x not in node.children:
                node.children[x] = TrieNode()
            node = node.children[x]
        node.end = True
        

    def search(self, word: str) -> bool:
        def dfs(idx, root):
            node = root
            for i in range(idx, len(word)):
                x = word[i]
                if x == ".":
                    for c in node.children.values():
                        if dfs(i + 1, c):
                            return True
                    return False
                else:
                    if x not in node.children:
                        return False
                    node = node.children[x]
            return node.end
        
        return dfs(0, self.root)
            
