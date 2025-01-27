'''
    GeeksforGeeks Daily Question (27-01-2025)
    LRU Cache
    Python3 solution
'''

class Node:
    def __init__(self, data, key):
        self.data = data
        self.key = key
        self.prev = None
        self.next = None
        
class LRUCache:
      
    #Constructor for initializing the cache capacity with the given value.  
    def __init__(self, cap):
        #code here
        self.mp = {}
        self.first = Node(-1, -1)
        self.last = Node(-1, -1)
        self.first.next = self.last
        self.last.prev = self.first
        self.cap = cap
        
    #Function to return value corresponding to the key.
    def get(self, key):
        #code here
        if key not in self.mp:
            return -1
        
        node = self.mp[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.mp[key]
        self.put(key, node.data)
        
        return self.first.next.data
        
    #Function for storing key-value pair.   
    def put(self, key, value):
        #code here
        if key in self.mp:
            node = self.mp[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            del self.mp[node.key]
        if len(self.mp) >= self.cap:
            node = self.last.prev
            node.prev.next = node.next
            node.next.prev = node.prev
            del self.mp[node.key]
        
        node = Node(value, key)
        self.mp[key] = node
        node.next = self.first.next
        self.first.next.prev = node
        self.first.next = node
        node.prev = self.first
        