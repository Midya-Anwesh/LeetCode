class dlNode:
    def __init__(self, key: int, val: int, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
    
    def __eq__(self, node) -> bool:
        if not isinstance(node, dlNode):
            return False
        return self.key == node.key

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.nodeMap = dict()
        self.head, self.tail, self.size = None, None, 0
    
    def deleteNode(self, node) -> None:
        if node is None:
            return 
        prevNode, nextNode = node.prev, node.next
        
        # First update head/tail
        if self.head is node:
            self.head = nextNode
        if self.tail is node:
            self.tail = prevNode

        # THEN patch neighbors
        if prevNode is not None:
            prevNode.next = nextNode
        if nextNode is not None:
            nextNode.prev = prevNode
    
    def append(self, node) -> None:
        node.prev = node.tail = None
        if self.tail is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
    
    def appendLeft(self, node) -> None:
        node.prev = node.next = None
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node


    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        node = self.nodeMap[key]
        self.deleteNode(node)
        self.appendLeft(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            node = self.nodeMap[key]
            self.deleteNode(node)
            self.appendLeft(node)
            node.val = value
            return
        if self.size >= self.cap:
            if self.tail is not None:
                toDel = self.tail.key
                self.deleteNode(self.tail)
                self.nodeMap.pop(toDel)
                self.size -= 1
            else:
                return
        newNode = dlNode(key, value)
        self.appendLeft(newNode)
        self.nodeMap[key] = newNode
        self.size += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)