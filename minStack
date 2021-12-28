class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
        print(self.stack)

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0:
            self.minStack.append(val)
            
        elif self.minStack[-1] >= val:
            self.minStack.append(val)
            
        

    def pop(self) -> None:
        if len(self.stack) > 0:
            val = self.stack.pop()
        if len(self.minStack) > 0:
            if val == self.minStack[-1]:
                self.minStack.pop()
        

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]

    def getMin(self) -> int:
        if len(self.minStack) > 0:
            return self.minStack[-1]        
        
obj = MinStack()
obj.push(1)
print(obj.top());
print("Min", obj.getMin());
obj.push(10)
print(obj.top());
print("Min", obj.getMin());
obj.push(0)
print(obj.top());
print("Min", obj.getMin());
print(obj.top());
obj.push(9)
print("Min", obj.getMin());
obj.pop()
obj.pop()
obj.push(11)
print(obj.top());
print("Min", obj.getMin());
print("Min", obj.getMin()); 