"""
- Stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle.
- You can only add or remove pancakes from the top.
- Basic operations we can do on a stack are:
    - Push: Adds a new element on the stack.
    - Pop: Removes and returns the top element from the stack.
    - Peek: Returns the top (last) element on the stack.
    - isEmpty: Checks if the stack is empty.
    - Size: Finds the number of elements in the stack.
"""



class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0



stack = Stack()

print(stack.size())

stack.push(1)
stack.push(2)

print(stack.size())
# print(stack.pop())
print(stack.size())

print(stack.peek())

