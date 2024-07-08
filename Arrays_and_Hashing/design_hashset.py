# No cheating... No constraints abuse... Enjoy!


class MyHashSet:

    def __init__(self):
        self.capacity = 2
        self.set = [None] * self.capacity
        self.size = 0

    def hash(self, key):
        return key % self.capacity

    def rehash(self):
        self.capacity *= 2
        new_set = [None] * self.capacity
        self.size = 0

        old_set = self.set
        self.set = new_set
        
        for key in old_set:
            if key is not None:
                for value in key:
                    self.add(value)

    def add(self, key: int) -> None:
        i = self.hash(key)
        
        if self.set[i] is None:
            self.set[i] = [key]
            self.size += 1
            if self.size >= self.capacity // 2:
                self.rehash()
        
        else:
            self.set[i].append(key)
        

    def remove(self, key: int) -> None:
        i = self.hash(key)

        if self.set[i] is not None:
            while key in self.set[i]:
                self.set[i].remove(key)
            self.size -= 1

    def contains(self, key: int) -> bool:
        i = self.hash(key)
        if self.set[i] is not None:
            return key in self.set[i]
        
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
