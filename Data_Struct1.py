class Stack:
    def __init__(self):
        self.StackPointer = -1
        self.Max = 4
        self.Contents = ["" for Elements in range(self.Max)]


    def Push(self, Item):
        self.StackPointer += 1
        if self.StackPointer >= 0:
            if self.StackPointer <= self.Max - 1:
                self.Contents[self.StackPointer] = Item
                return True
            else:
                self.StackPointer -= 1
                return False
        else:
            return False


    def Pop(self):
        
        if self.StackPointer >= 0:
            Item = self.Contents[self.StackPointer]
            self.Contents[self.StackPointer] = ""
            self.StackPointer -= 1
            return Item
        else:
            return None

   
    def Peek(self):
        if self.StackPointer >= 0:
            Item = self.Contents[self.StackPointer]
            return Item
        else:
            return None
        
def ClearStack(InputStack):
    Item = InputStack.Peek()
    while Item:
        Item = InputStack.Pop()
        if Item:
            print(Item)

if __name__ == "__main__":
    stack = Stack()

    for i in range(5):
        print(stack.Push(i))
    for i in range(3):
        print(stack.Pop())
    print(stack.Contents)
    print(stack.Peek())
    