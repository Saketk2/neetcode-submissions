class LinkedList:

    def __init__(self, key = None):
        self.key = key
        self.nxt = None

class MyHashSet:

    def __init__(self):
        self.vals = LinkedList()
        
    def add(self, key: int) -> None:
        if self.contains(key):
            return
        val = LinkedList(key)
        val.nxt = self.vals.nxt
        self.vals.nxt = val
        
    def remove(self, key: int) -> None:
        curr = self.vals
        prev = LinkedList()
        while curr:
            if curr.key == key:
                prev.nxt = curr.nxt
                curr.nxt = None
                return
            else:
                prev = curr
                curr = curr.nxt    
        
    def contains(self, key: int) -> bool:
        curr = self.vals
        while curr:
            if curr.key == key:
                return True
            else:
                curr = curr.nxt
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)