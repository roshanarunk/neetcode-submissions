class Node:
    def __init__(self, key=0, val=0):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.front = Node()
        self.back = Node()
        self.front.next, self.back.prev = self.back, self.front
        self.size = 0
        
    def insert(self, node):
        prev, next = self.back.prev, self.back
        prev.next, next.prev = node, node
        node.prev, node.next = prev, next

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val
        
        

    def put(self, key: int, value: int) -> None:
        node = None
        if key not in self.cache:
            node = Node(key, value)
            self.cache[key] = node
            self.size += 1
        else:
            node = self.cache[key]
            node.val = value
            self.remove(node)
        self.insert(node)
        

        if self.size > self.capacity:
            removal = self.front.next
            self.remove(removal)
            del self.cache[removal.key]
            self.size -= 1
        
                


        
