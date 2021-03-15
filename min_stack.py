class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.minval = None
        

    def push(self, x: int) -> None:
        if len(self.data) == 0 or x < self.minval:
            self.minval = x
        self.data.append(x)

    def pop(self) -> None:
        self.data.pop()
        self.minval = min(self.data)

    def top(self) -> int:
        return self.data.pop()

    def getMin(self) -> int:
        return self.minval


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()