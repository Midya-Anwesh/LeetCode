# runtime = 155.0ms
# memory usage = 19.7MB

class MyHashMap:

    def __init__(self):
        self.h_map = dict()
        return

    def put(self, key: int, value: int) -> None:
        self.h_map.update({key:value})

    def get(self, key: int) -> int:
        return self.h_map.get(key,-1)
        

    def remove(self, key: int) -> None:
        self.h_map.pop(key,None)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)