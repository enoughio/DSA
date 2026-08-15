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

# --------------


class MyHashMap:

    def __init__(self):
        self.cap = int(10e5) + 3
        self.dec = [None] * self.cap

    def put(self, key: int, value: int) -> None:
        self.dec[key] = value            

    def get(self, key: int) -> int:
        if self.dec[key] is None :
            return -1 
        return self.dec[key]

    def remove(self, key: int) -> None:
        if self.dec[key] is not None :
            self.dec[key] = None
        return None

