class LinkedList:

    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.nxt = None

class MyHashMap:

    def __init__(self):
        self.vals = LinkedList()
        
    def put(self, key: int, value: int) -> None:
        if self.contains(key):
            head = self.vals
            while head:
                if head.key == key:
                    head.value = value
                    return
                head = head.nxt
        else:
            new = LinkedList(key, value)
            new.nxt = self.vals.nxt
            self.vals.nxt = new

    def get(self, key: int) -> int:
        if self.contains(key):
            head = self.vals
            while head:
                if head.key == key:
                    return head.value
                head = head.nxt
        return -1

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        head = self.vals
        prev = LinkedList()
        while head:
            if head.key == key:
                prev.nxt = head.nxt
                head.nxt = None
                return
            prev = head
            head = head.nxt

    def contains(self, key: int) -> bool:
        head = self.vals
        while head:
            if head.key == key:
                return True
            head = head.nxt
        return False
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)