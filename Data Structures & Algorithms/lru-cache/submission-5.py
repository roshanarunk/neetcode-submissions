class Node:
    def __init__(self, key=0, value=0):
        self.next = None
        self.prev = None
        self.key = key
        self.value = value

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.front, self.back = Node(), Node()
        self.front.next, self.back.prev = self.back, self.front
        self.cache = {}

    def insert(self, node):
        prev, next = self.back.prev, self.back
        node.prev, node.next = prev, next
        prev.next, next.prev = node, node

    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.cache[key] = Node(key, value)
            self.size += 1
        else:
            self.remove(self.cache[key])
        node = self.cache[key]
        node.value = value
        self.insert(node)

        if self.size > self.capacity:
            lastUsed = self.front.next
            self.remove(lastUsed)
            del self.cache[lastUsed.key]
            self.size -= 1


        
