class MyHashSet:

    def __init__(self):
        self.cap = 10**5 + 1
        self.nums =  [False] * self.cap
        self.cnt = 0

    def add(self, key: int) -> None:
         if self.nums[key] is False : 
            self.nums[key] = True
 
    def remove(self, key: int) -> None:
        if self.nums[key] is True : 
            self.nums[key] = False

    def contains(self, key: int) -> bool:
        if self.nums[key] is True : 
            return True
        return False

