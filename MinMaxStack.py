class MinMaxStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.maxStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0 or val <= self.minStack[-1]:
            self.minStack.append(val)
        if len(self.maxStack) == 0 or val >= self.maxStack[-1]:
            self.maxStack.append(val)

    def pop(self) -> None:
        if len(self.stack) > 0:
            val = self.stack.pop()
        if len(self.minStack) > 0 and val == self.minStack[-1]:
            self.minStack.pop()
        if len(self.maxStack) > 0 and val == self.maxStack[-1]:
            self.maxStack.pop()

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        if len(self.minStack) > 0:
            return self.minStack[-1]
        else:
            return None
    def getMax(self) -> int:
        if len(self.maxStack) > 0:
            return self.maxStack[-1]
        else:
            return None


obj = MinMaxStack()
obj.push(1)
obj.push(0)
print('min', obj.getMin())
print('max', obj.getMax())
print('top', obj.top())
obj.push(-1)
print('min', obj.getMin())
print('max', obj.getMax())
print('top', obj.top())
obj.pop()
print('min', obj.getMin())
print('top', obj.top())
print('max', obj.getMax())
obj.pop()
obj.pop()
obj.pop()
print('top', obj.top())
print('min', obj.getMin())
print('max', obj.getMax())
obj.push(20)
obj.push(9)
obj.push(99)
print('top', obj.top())
print('min', obj.getMin())
print('max', obj.getMax())