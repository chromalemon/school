class Stack:
    def __init__(self):
        self.stack = [0 for i in range(11)]
        self.pointer = -1

    def push(self, val):
        if self.pointer <= 10:
            self.pointer += 1
            self.stack[self.pointer] = val
            return 1
        else:
            return 0 
        
    def pop(self):
        if self.pointer >= 0:
            self.pointer -= 1
            return self.stack[self.pointer + 1]
        else:
            return None
        
    def peek(self):
        if self.pointer >= 0:
            return self.stack[self.pointer]
        else:
            return None
        
    def get_stack(self):
        stack = []
        for i in range(self.pointer + 1):
            stack.append(self.stack[i])
        return stack
    
    def size(self):
        return self.pointer + 1
    
    def is_empty(self):
        return self.pointer == -1
        
stack1 = Stack()
stack1.push(3)
print(stack1.get_stack())
stack1.push(4)
print(stack1.get_stack())
print(stack1.peek())
stack1.pop()
print(stack1.get_stack())
