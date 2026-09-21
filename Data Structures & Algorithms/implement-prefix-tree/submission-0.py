class PrefixTree:

    def __init__(self):
        self.root = {}
        self.term = "$"

    def insert(self, word: str) -> None:
        node = self.root
        for x in word:
            if x in node:
                node = node[x]
            else:
                node[x] = {}
                node = node[x]
        node[self.term] = {}


    def search(self, word: str) -> bool:
        node = self.root
        for x in word:
            if x not in node:
                return False
            else:
                node = node[x]
        if self.term in node:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for x in prefix:
            if x not in node:
                return False
            else:
                node = node[x]
        return True
        