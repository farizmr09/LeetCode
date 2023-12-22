import random

class RandomizedSet:
    
    def __init__(self):
        self.list = []

    def insert(self, val: int) -> bool:
        if self.list.count(val):
            return False
        self.list.append(val)
        return True
    
    def remove(self, val: int) -> bool:
        try:
            self.list.remove(val)
            return True
        except:
            return False

    def getRandom(self) -> int:
        return self.list[random.randint(0, len(self.list) - 1)]
