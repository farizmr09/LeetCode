class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity        
        self.cache = {}

    def get(self, key: int) -> int:
        if self.cache.get(key) != None:
            self.cache[key] = self.cache.pop(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.cache.pop(key, -1)
        self.cache[key] = value
        if len(self.cache.values()) > self.capacity:
            self.cache.pop(list(self.cache.keys())[0])
            
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)