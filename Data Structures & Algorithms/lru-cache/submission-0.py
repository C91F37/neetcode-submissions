class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.prev,self.nxt = None, None
class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.nxt=self.right
        self.right.prev=self.left

    def insert(self, node):
        p = self.right.prev
        r = self.right
        node.nxt = r
        node.prev = p
        p.nxt = node
        r.prev = node
    def remove(self, node):
        n=node.nxt
        p=node.prev
        n.prev=p
        p.nxt=n
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        n = self.cache[key]
        self.remove(n)
        self.insert(n)
        return self.cache[key].v

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].v=value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        else:
            n=Node(key,value)
            self.cache[key]=n
            self.insert(n)
        if len(self.cache) > self.capacity:
            del self.cache[self.left.nxt.k]
            self.remove(self.left.nxt)
