



class Stack:

    def __init__(self):
        self.stack = []

    
    def push(self, element):
        self.stack.append(element)

    def pop(self):
        self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def is_empty(self):
        return bool(len(self.stack) < 0)
    
    def size(self):
        return len(self.stack)
    


stack = Stack()

print(stack.push(1))
print(stack.is_empty())
print(stack.size())
print(stack.peek())
print(stack.pop())



