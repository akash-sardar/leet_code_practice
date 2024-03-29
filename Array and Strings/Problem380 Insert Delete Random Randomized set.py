class RandomizedSet:

    def __init__(self):
        self.s1 = set()

    def insert(self, val: int) -> bool:
        self.val = val
        s1 = self.s1
        m = len(s1)
        s1.add(val)
        if len(s1) == m:
            return False
        else:
            return True

    def remove(self, val: int) -> bool:
        self.val = val
        s1 = self.s1
        m = len(s1)
        try:
            s1.remove(val)
            return True
        except:
            return False

    def getRandom(self) -> int:
        s1 = self.s1
        return random.choice(list(s1))

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()