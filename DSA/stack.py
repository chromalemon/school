class Stack:
    def __init__(self):
        self.stack = []
        self.pointer = -1

    def push(self, val):
        if self.pointer <= 10:
            self.stack.append(val)
            self.pointer += 1
            return 1
        else:
            return 0 
        
    def pop(self):
        if self.pointer >= 0:
            self.stack.pop(-1)
            self.pointer -= 1
            return 1
        else:
            return 0 
        
    def peek(self):
        if self.pointer >= 0:
            return self.stack[-1]
        else:
            return 0 
        
    def get_stack(self):
        return self.stack
    
    def size(self):
        return len(self.stack)
        
stack1 = Stack()
stack1.push(3)
print(stack1.get_stack())
stack1.push(4)
print(stack1.get_stack())
stack1.peek()
stack1.pop()
print(stack1.get_stack())
