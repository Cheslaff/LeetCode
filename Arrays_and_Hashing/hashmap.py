class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val


class MyHashMap:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.map = [None] * self.capacity

    def hash(self, key):
        return key % self.capacity

    def rehash(self):
        self.capacity = 2 * self.capacity
        newMap = []
        for i in range(self.capacity):
            newMap.append(None)

        oldMap = self.map
        self.map = newMap
        self.size = 0
        for pair in oldMap:
            if pair:
                self.put(pair.key, pair.val)

    def put(self, key: int, value: int) -> None:
        i = self.hash(key)

        while True:
            if self.map[i] is None:
                self.map[i] = Pair(key, value)
                self.size += 1

                if self.size >= self.capacity // 2:
                    self.rehash()
                return

            elif self.map[i].key == key:
                self.map[i].val = value
                return

            i += 1
            i = i % self.capacity

    def get(self, key: int) -> int:
        i = self.hash(key)

        while self.map[i] is not None:
            if self.map[i].key == key:
                return self.map[i].val
            i += 1
            i = i % self.capacity
        return -1

    def remove(self, key: int) -> None:
        if self.get(key) == -1:
            return

        i = self.hash(key)
        while True:
            if self.map[i].key == key:
                self.map[i] = None
                self.size -= 1
                return
            i += 1
            i = i % self.capacity




# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
