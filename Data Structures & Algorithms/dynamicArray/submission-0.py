class DynamicArray:
    def __init__(self, capacity: int):
        self.arr = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n
        # newSize = self.size + 1
        # if newSize > self.capacity:
        #     self.resize()

        # cur = self.size
        # while cur >= i:
        #     self.arr[cur] = self.arr[cur - 1]
        # self.arr[i] = n
        # self.size = newSize

    def pushback(self, n: int) -> None:
        newSize = self.size + 1
        if newSize > self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size = newSize

    def popback(self) -> int:
        val = self.arr[self.size - 1]
        self.arr[self.size - 1] = 0
        self.size -= 1
        return val

    def resize(self) -> None:
        newCapacity = self.capacity * 2
        arr = [0] * newCapacity
        for i in range(self.size):
            arr[i] = self.arr[i]
        self.arr = arr
        self.capacity = newCapacity

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity
