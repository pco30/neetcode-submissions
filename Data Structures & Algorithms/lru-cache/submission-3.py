# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cap = capacity
#         self.cache = OrderedDict()
        

#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#         self.cache.move_to_end(key)
#         return self.cache[key]
        

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.cache.move_to_end(key)
#         self.cache[key] = value

#         if len(self.cache) > self.cap:
#             self.cache.popitem(last=False)
        



class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node):  # A - B - *C - D
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    
    def add(self, node):  # A - B - *C - tail
        prev = self.tail.prev
        nxt = self.tail
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node
    
    def get(self, key):
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.value
    
    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        
        node = Node(key, value)
        self.cache[key] = node
        self.add(node)

        if len(self.cache) > self.cap:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]
    


















