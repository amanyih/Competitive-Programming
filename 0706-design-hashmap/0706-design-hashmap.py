class MyHashMap:

    def __init__(self):
        
        self.mapping = [None] * (10 **6 + 1)

    def put(self, key: int, value: int) -> None:
        self.mapping[key] = value
        
    def get(self, key: int) -> int:
        return self.mapping[key] if self.mapping[key] != None else -1
        
    def remove(self, key: int) -> None:
        self.mapping[key] = None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)